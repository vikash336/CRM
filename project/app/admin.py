from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Lead, User_BD,GenderAll, Contact



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    ordering = ['email']

admin.site.register(Lead)
admin.site.register(Contact)
admin.site.register(GenderAll)
admin.site.register(User_BD)
admin.site.register(CustomUser, CustomUserAdmin)