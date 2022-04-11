from calendar import timegm
from cmath import e
from datetime import datetime, timedelta
import email
from urllib import response
from itsdangerous import json

import jwt
from django.conf import settings
# Create your views here.
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.http import Http404, HttpResponse
from django.utils import timezone
from flask_login import user_logged_in
from rest_framework import authentication, permissions, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_payload_handler
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from signupapi import settings
from sqlalchemy import false

from account import serializers

from .models import Login, account, token
from .serializers import accountSerializer, loginSerializer


class accountView(viewsets.ModelViewSet):
    serializer_class = accountSerializer
    permission_classes = (AllowAny,IsAuthenticated)
    queryset = account.objects.all()
    




    

class loginView(APIView):

    def post(self,request,format=None):
        authentication_classes = (authentication.SessionAuthentication,)
        permission_classes = (permissions.IsAuthenticated,)
        serializer = loginSerializer(data=request.data)
        if serializer.is_valid():
            print('working!')
            print(serializer.data)
    
        try:
            user = account.objects.get(email=serializer.data['email'],password=serializer.data['password'])
            if user:
                try:
                    payload = jwt_payload_handler(user)
                    
                    token = jwt.encode(payload, settings.SECRET_KEY)
                    print(token)
                
                    user_details = {}
                    user_details['details'] = "%s %s" % (
                        user.email, user.password)
                    user_details['token'] = token
                    print(token)
                    user_logged_in.send(sender=user.__class__,
                                        request=request, user=user,token=token)
                    return Response(user_details,status=status.HTTP_200_OK)
    
                except Exception as e:
                    raise e
            else:
                res = {
                    'error': 'can not authenticate with the given credentials or the account has been deactivated'}
                return Response(res, status=status.HTTP_403_FORBIDDEN)
        except KeyError:
            res = {'error': 'please provide a email and a password'}
            return Response(res)











    # def post(self, request, format=None):
    #     serializer = loginSerializer(data=request.data)
    #     if serializer.is_valid():
    #         # serializer.save()
    #         print('working!')
    #         print(serializer.data)
    #         try:
    #             values=account.objects.get(email=serializer.data['email'],password=serializer.data['password'])
    #             print(values)    
    #         except Exception as e:
    #             print('exception occured')  
    #             print(type(e).__name__)  
    #             if type(e).__name__ == 'DoesNotExist':
    #                 return Response('please register with email', status=status.HTTP_401_UNAUTHORIZED)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     # return Response(serializer.initial_data, status=status.HTTP_201_CREATED)    

