from django.urls import path,include
from django.contrib import admin

# from account.models import account
from .router import router
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .models import account

urlpatterns = [ 
    path("",include(router.urls)),
    path('Login/', views.loginView.as_view()),
   
]
