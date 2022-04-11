from datetime import timedelta
from pyexpat import model
from tkinter import Widget
from django.db import models
from django.forms import PasswordInput
from sqlalchemy import null
from django.db import transaction
from rest_framework import serializers
from cryptography.fernet import Fernet
import jwt
from django.utils import timezone
from django.conf import settings
from datetime import datetime
from rest_framework_simplejwt.tokens import RefreshToken

class account(models.Model):
   first_name = models.CharField(max_length=100)
   last_name= models.CharField(max_length=100)
   email=models.EmailField(max_length=100)
   password = models.CharField(max_length=100)
   passwordconform  = models.CharField(max_length=100)
   

   def __str__(self):
      return self.password

class Login(models.Model):
   email= models.CharField(max_length=100)
   password=models.CharField(max_length=100)

   def __str__(self):
      return self.email

@property
def token(self):
   token = jwt.encode({'email':self.email,
   'exp': datetime.utcnow() + timedelta(minutes=1)},
   settings.SECRET_KEY,algorithm='HS256') 
   return token  


# class Logintracking():
#    token=models.CharField(max_length=100)

#    def __str__(self):
#       return self.token
