from django.db import models

# Create your models here.
class User_Auth(models.Model):
    password = models.CharField(max_length=300,default="")
    Name = models.CharField(max_length=30,default="")
    Phone = models.CharField(max_length=12,default="")
    username = models.CharField(max_length=20,default="")
    Email = models.CharField(max_length=50)
    # last_login_time = models.CharField(max_length=20,default="")
    # auth_token = models.CharField(max_length=50,default="")
    # is_owner = models.IntegerField(null = True)
    # is_user = models.IntegerField(null = True)
    who = models.CharField(max_length=10,default="")
    gst_num = models.CharField(max_length=20,default="")
    # login_status = models.BooleanField(default=False)
    profile_status = models.BooleanField(default=False)


class Login_User(models.Model):
    loggeduser = models.CharField(max_length=20,default="")
    auth_token = models.CharField(max_length=50,default="")
    userid = models.IntegerField()

class e_wallet(models.Model):
    balance = models.IntegerField(default=0)
    user = models.IntegerField(null=True)
    wallet_status = models.BooleanField(default=False)


class otp_verify(models.Model):
    user = models.CharField(max_length=20,default="")
    otp = models.IntegerField()

# class transactions(models.Model):
    
#     user = models.ForeignKey(User_Auth,on_delete=models.CASCADE)

class left_pannel(models.Model):
    field = models.CharField(max_length=30)
    for_user = models.IntegerField()
    for_owner = models.IntegerField()
    url = models.CharField(max_length=30,default="")
    priority = models.IntegerField(default=0)
    icons = models.CharField(max_length=30,default="")