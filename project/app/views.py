from django.shortcuts import render
from .serializers import Lead_serializer , User_serializer
from rest_framework.decorators import APIView
from .models import Lead , CustomUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
import datetime
import jwt
from django.contrib.auth.hashers import make_password
from project.settings import SECRET_KEY
class CR(APIView):
    def post(slef, request):
        f1=request.data
        f2=Lead_serializer(data=f1)
        if f2.is_valid(raise_exception=True):
            f2.save()
            return Response(
                f2.data
            )
        return Response(Lead_serializer.errors(), status=status.HTTP_400_BAD_REQUEST)

class Regiter(APIView):
    def post(self,request):
        data=request.data
        pwd_hash=make_password(data['password'])
        data['password']=pwd_hash
        serializer = User_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user_data1 = CustomUser.objects.filter(email=email).first()
        # user_data = authenticate(email=email, password=password)
        if user_data1.check_password(password) is False:
            raise AuthenticationFailed({
                "Status": "Incorrect Password"
            })
        if user_data1.check_password(password) is True:
            payload = {
                'id': user_data1.id,
                'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=100),
                'iat': datetime.datetime.utcnow()

            }
            ALGORITHM = "HS256"
            encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
            response = Response()

            response.set_cookie(key='jwt', value=encoded_jwt)
            response.data = {
                'jwt': encoded_jwt
            }
            return response

class Operations(APIView):
    def post(self,request):
        pass
