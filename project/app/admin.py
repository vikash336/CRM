from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Lead



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    ordering = ['email']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Lead)