# from django.contrib import admin
from django.urls import path
from user import views
urlpatterns = [
    path('otp', views.otp_gen),
    path('register',views.register),
    path('login',views.Login)
]