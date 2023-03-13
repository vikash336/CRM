from rest_framework import serializers
from .models import CustomUser , Contact , Lead , Lead_Sourcer , Lead_status , GenderAll, User_BD, Industry


class User_serializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields = ['id', 'email', 'password','first_name', 'last_name', 'role']


class Lead_serializer(serializers.ModelSerializer):
    class Meta:
        model=Lead
        fields=('__all__')


class BD_serializer(serializers.ModelSerializer):

    # Gender=serializers.CharField(max_length=100)
    # associateds=serializers.CharField(max_length=100)
    class Meta:
        model=User_BD
        fields=['Gender', 'Name', 'associateds']