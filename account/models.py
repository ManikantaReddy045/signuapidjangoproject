from tkinter import Widget
from django.db import models
from django.forms import PasswordInput
from sqlalchemy import null
from django.db import transaction
from rest_framework import serializers


class account(models.Model):
   first_name = models.CharField(max_length=100)
   last_name= models.CharField(max_length=100)
   email=models.EmailField(max_length=100)
   password = models.CharField(max_length=100)
   passwordconform  = models.CharField(max_length=100)
 
   def __str__(self):
    return self.email
