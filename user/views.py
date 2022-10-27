from django.shortcuts import render
from .models import User_Auth,e_wallet,otp_verify,left_pannel
from django.http import JsonResponse
import json
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
from random import randint
from datetime import datetime
import cryptocode
import random
import string


def otp_gen(request):
    if(request.method == 'POST'):
        data = json.loads(request.body)
        print(data)
        otp = randint(100000,999999)
        subject = 'OTP Verification'
        message = f'Your OTP for verification is : {otp}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [data['email']]
        send_mail( subject, message, email_from, recipient_list )
        insdata = list(otp_verify.objects.filter(user=data['username']))
        if(len(insdata)!=0):
            ins = otp_verify.objects.get(user=data['username'])
            ins.otp=otp
            ins.save()
        else:
            otp_verify.objects.create(user=data['username'],otp=otp)
        return JsonResponse({'msg':'otp generated'},status=200)
    else:
        return JsonResponse({'msg':'bad request'},status=400)

def register(request):
    if(request.method == 'POST'):
        data = json.loads(request.body)
        insdata = list(User_Auth.objects.filter(username=data['username']))
        if(len(insdata) != 0):
            return JsonResponse({'msg':'user already exists'},status=406)
        getotp = list(otp_verify.objects.filter(user=data['username'])) 
        print(getotp[0].otp)
        if(int(data['otp']) == getotp[0].otp): 
            encpass = cryptocode.encrypt(data['password'], settings.HASHKEY)
            User_Auth.objects.create(username=data['username'],Email=data['email'],password=encpass)
            return JsonResponse({'msg':'Registration Successfull'},status=200)
        else:
            return JsonResponse({'msg':'wrong otp'},status=406)

def Login(request):
    if(request.method == 'POST'):
        data = json.loads(request.body)
        insdata = list(User_Auth.objects.filter(username=data['username']))
        if(len(insdata) == 0):
            return JsonResponse({'msg':'Username Not Found'},status=406)
        else:
            pas = cryptocode.decrypt(insdata[0].password, settings.HASHKEY)
            if(pas == data['password']):
                print('Logged in')
                now = datetime.now()
                dt = now.strftime("%d/%m/%Y %H:%M:%S")
                access = ''.join(random.choices(string.ascii_lowercase + string.digits, k=settings.NUM))
                upd = User_Auth.objects.get(username=data['username'])
                upd.auth_token = access
                upd.last_login_time = dt
                upd.login_status = True
                upd.save()
                return JsonResponse({'access':access},status=200)
            else:
                return JsonResponse({'msg':'Wrong Password'},status=406)
    else:
        return JsonResponse({'msg':'Bad Request'},status=400)