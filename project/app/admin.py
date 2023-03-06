from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Lead, User_BD,GenderAll, Contact , Lead_status ,Industry, Lead_Sourcer



# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ['email', 'first_name', 'last_name', 'is_staff']
#     ordering = ['email']


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Lead)
admin.site.register(Lead_status)
admin.site.register(Industry)
admin.site.register(Lead_Sourcer)
admin.site.register(Contact)
admin.site.register(GenderAll)
admin.site.register(User_BD)