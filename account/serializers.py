from typing_extensions import Required
from wsgiref.validate import validator
from rest_framework import serializers
from .models import account
from django.db import transaction

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


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

    # def create(self, validated_data):
    # # confirm_password should not be sent to create as it is not part of User model
    #     validated_data .pop('passwordconform')
    #     return super(User, self).create(validated_data)    



    # def create(self, validated_data):
    #     print('function executed')

    
    #     user = account(
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name'] ,
    #         email=validated_data['email'],  
           
    #     )
    #     print(account)
    #     account(validated_data['password']),
    #     account.save()
    #     return account
    
    