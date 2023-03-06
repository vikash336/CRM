from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email



LeadStatus =(
    ("1", "Active"),
    ("2", "Hold"),
    ("3", "Reject"),
    ("4", "Pending"),
)


class Industry(models.Model):
    Industry=models.CharField(max_length=100)

    def __str__(self):
        return self.Industry
class Lead_status(models.Model):
    status=models.CharField(max_length=100)

    def __str__(self):
        return self.status


class GenderAll(models.Model):
    type=models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.type
class User_BD(models.Model):
    Gender=models.ForeignKey(GenderAll, on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)

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
    phone_no = PhoneNumberField()
    accountstatus = models.BooleanField(default=False)
    website=models.CharField(max_length=100,default='None')
    skypeID=models.CharField(max_length=100 )
    No_of_rescorce_deployed=models.PositiveIntegerField(default='0')
    # leadstatus = models.CharField(
    #     max_length=20,
    #     choices=LeadStatus,
    #     default='N/A'
    # )
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