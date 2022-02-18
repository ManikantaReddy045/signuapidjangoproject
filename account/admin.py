from django.contrib import admin
from .models import account

class accountAdmin(admin.ModelAdmin):
  list = ('first_name','last_name','email','password','passwordconform')

admin.site.register(account, accountAdmin)
