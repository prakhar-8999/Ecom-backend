from django.db import models

# Create your models here.
class User_Auth(models.Model):
    password = models.CharField(max_length=300,default="")
    Name = models.CharField(max_length=10,default="")
    Phone = models.IntegerField(null = True)
    username = models.CharField(max_length=20,default="")
    Email = models.CharField(max_length=50)
    last_login_time = models.CharField(max_length=20,default="")
    auth_token = models.CharField(max_length=50,default="")
    is_owner = models.IntegerField(null = True)
    is_user = models.ImageField(null = True)
    gst_num = models.CharField(max_length=10,default="")
    login_status = models.BooleanField(default=False)
    profile_status = models.BooleanField(default=False)

class e_wallet(models.Model):
    balance = models.IntegerField(default=0)
    user = models.ForeignKey(User_Auth,on_delete=models.CASCADE)
    wallet_status = models.BooleanField(default=False)


class otp_verify(models.Model):
    user = models.CharField(max_length=20,default="")
    otp = models.IntegerField()

# class transactions(models.Model):
    
#     user = models.ForeignKey(User_Auth,on_delete=models.CASCADE)

class left_pannel(models.Model):
    field = models.CharField(max_length=10)
    for_user = models.IntegerField()
    for_owner = models.IntegerField()