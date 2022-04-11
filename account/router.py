from rest_framework import routers
from .views import accountView
from django.urls import path,include
# from .views import loginView

router=routers.DefaultRouter()
router.register('account',accountView)



urlpatterns = [
    path("",include(router.urls))
]
