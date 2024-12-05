from django.contrib import admin

# Register your models here.
from .models import User, userdetails

# admin.site.register(User)
admin.site.register(userdetails)
