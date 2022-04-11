"""signupapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.db import router
from django.urls import path,include
from rest_framework import routers
from account import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register(r'account', views.accountView, 'account')
# router.register(r'Login',views.loginView,'Login')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('account',include('account.urls')),
    path('',include(router.urls)),
    path('Login/', views.loginView.as_view()),
    path('account/', views.account, name="email"),

    
    # path('login/token', views.loginView.as_view(), name='login'),
    # path('login/token', views.loginView.as_view(), name='login_refresh'),


    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)