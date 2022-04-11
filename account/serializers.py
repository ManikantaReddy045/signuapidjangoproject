from cgi import print_directory
from dataclasses import fields
from django.shortcuts import render
from email import message
from operator import attrgetter
from pyexpat.errors import messages
from sre_constants import SUCCESS
from tkinter.tix import Select
from typing_extensions import Required
from wsgiref import validate
from wsgiref.validate import validator
from attr import attr, attrs
from defer import return_value
from django.shortcuts import redirect
from flask import request
from rest_framework import serializers
from sqlalchemy import false
from .models import account
from django.db.models import Count, F
from django.shortcuts import  render, redirect
from django.db import transaction
from .models import Login
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib import auth
from django.contrib.auth import login, authenticate
from account import models





class accountSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=account.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    passwordconform = serializers.CharField(write_only=True, required=True,validators=[validate_password])    
    
    class Meta:
        model = account
        fields = ('id','first_name','last_name','email','password','passwordconform')
        extra_kwargs = {'password': {'write_only': True}}
       

    def validate(self, attrs):
        if attrs['password'] != attrs['passwordconform']:
            raise serializers.ValidationError({"passwordconform": "Password  didn't match."})
        return  attrs

class loginSerializer(serializers.ModelSerializer):

    class Meta:
        model = account
        fields = ('id','email','password')

        
# class loginvalidation(serializers.ModelSerializer):
#     class Meta:
#         model = Login
#         fields =('token')