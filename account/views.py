from sys import modules
from django.shortcuts import redirect, render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import accountSerializer
from rest_framework import viewsets
from .models import account
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.



class accountView(viewsets.ModelViewSet):
    serializer_class = accountSerializer
    permission_classes = (AllowAny,)
    queryset = account.objects.all()

