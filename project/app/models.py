from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('USER', 'User'),
        ('STAFF', 'Staff'),
        ('ADMIN', 'Admin'),
    ]

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='USER')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.first_name

    def has_role(self, role):
        return self.role == role

    def has_permission(self, perm):
        return self.user_permissions.filter(codename=perm).exists() or \
            self.groups.filter(permissions__codename=perm).exists()

    @property
    def is_user(self):
        return self.has_role('USER')

    @property
    def is_staff_lead(self):
        return self.has_role('STAFF')

    @property
    def is_admin(self):
        return self.has_role('ADMIN')

class Record(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='records')

    def __str__(self):
        return self.name

class Industry(models.Model):
    Industry=models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.Industry
class Lead_status(models.Model):
    status=models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.status


class GenderAll(models.Model):
    type=models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.type
class User_BD(models.Model):
    Gender=models.ForeignKey(GenderAll, on_delete=models.CASCADE)
    Name=models.CharField(max_length=100, primary_key=True)
    associateds=models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.Name


class Lead_Sourcer(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name

class Lead(models.Model):
    leadName = models.CharField(max_length=100, unique=True)
    Title=models.CharField(max_length=100)
    Contact = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    accountstatus = models.BooleanField(default=False)
    website=models.CharField(max_length=100,default='None')
    skypeID=models.CharField(max_length=100 )
    No_of_rescorce_deployed=models.PositiveIntegerField(default='0')
    lead_Status=models.ForeignKey(Lead_status, on_delete=models.CASCADE, related_name='Lead_Status' )
    lead_Sourcer = models.ForeignKey(User_BD, on_delete=models.CASCADE, related_name='Lead_UserBD')
    lead_Source=models.ForeignKey(Lead_Sourcer, on_delete=models.CASCADE, related_name='Lead_sourcer')
    Industry=models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='Lead_Industry')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title


class Contact(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='lead_contact' )
    contact_first_name = models.CharField(max_length=255)
    contact_last_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    skype_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.lead)

