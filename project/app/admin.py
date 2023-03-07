from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Lead, User_BD,GenderAll, Contact , Lead_status ,Industry, Lead_Sourcer,Record



class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'role')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'role')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'role')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'role'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'owner')
    list_filter = ('owner__email',)
    search_fields = ('name', 'description')
    ordering = ('name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_admin:
            return qs
        elif request.user.is_staff_lead:
            return qs.filter(owner__in=request.user.subordinates.all())
        else:
            return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.owner = request.user
        super().save_model(request, obj, form, change)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Lead)
admin.site.register(Lead_status)
admin.site.register(Industry)
admin.site.register(Lead_Sourcer)
admin.site.register(Contact)
admin.site.register(GenderAll)
admin.site.register(User_BD)