from django.shortcuts import render
from rest_framework import viewsets
# from .models import User
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import EmailMultiAlternatives
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string, get_template
from django.template import Context
from rest_framework.decorators import authentication_classes, permission_classes

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
import email.message
from rest_framework import permissions
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
import smtplib
import random
import string
from django.utils import timezone
from django.contrib.postgres.search import SearchVector
from decouple import config
from rest_framework import filters
from rest_framework import permissions


from .models import User
from .serializers import UserSerializer,GetUserSerializer



class GetUserView(generics.GenericAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    def get(self,request,format=None):
        try:
            user=User.objects.get(id=self.request.user.id)
            print(self.request.user.id)
            user_serializer=GetUserSerializer(user)
            user_data = user_serializer.data
            return Response(status=status.HTTP_200_OK,data=user_data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])


class Signup(generics.GenericAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.AllowAny]
    def post(self,request,format=None):
        try:
            message = get_template('verification.html').render({"email":request.data.get('email')})
            msg = EmailMultiAlternatives('Verification', message,'autootoncst@gmail.com', [request.data.get('email')])
            html_content = '<p>This is an <strong>important</strong> message.</p>'
            msg.content_subtype = "html"
            msg.send()
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])

class OTP(generics.GenericAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.AllowAny]
    def post(self,request,format=None):
        try:
            message = get_template('otp.html').render({"code":request.data.get('code')})
            msg = EmailMultiAlternatives('OTP', message,'autootoncst@gmail.com', [request.data.get('email')])
            html_content = '<p>This is an <strong>important</strong> message.</p>'
            msg.content_subtype = "html"
            msg.send()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])


class CheckEmail(generics.GenericAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.AllowAny]
    def post(self,request,format=None):
        try:
            item = User.objects.filter(email=request.data.get('email')).count()
            print(item)
            if(item==0):
                return Response(status=status.HTTP_200_OK,data={'status':'valid'})
            else:
                return Response(status=status.HTTP_200_OK,data={'status':'invalid'})
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])

class UserActivation(generics.GenericAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.AllowAny]
    def post(self,request,format=None):
        try:
            message = get_template('Activation.html').render({})
            msg = EmailMultiAlternatives('Activation', message,'autootoncst@gmail.com', [request.data.get('email')])
            html_content = '<p>This is an <strong>important</strong> message.</p>'
            msg.content_subtype = "html"
            msg.send()
            # serializer = UserSerializer(data=request.data)
            # serializer.is_valid(raise_exception=True)
            # serializer.save()
            User.objects.filter(id=request.data.get('id')).update(is_active=True)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])
        

class UserVerification(generics.GenericAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.AllowAny]
    def get(self,request,format=None,email=None):
        try:
            print('okay')
            User.objects.filter(email=email).update(is_verified=True)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])

class UserView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    filter_backends = [filters.SearchFilter]    
    search_fields = ['name']
    
    @swagger_auto_schema(method="patch", request_body=UserSerializer)
    @action(detail=True, methods=["PATCH"])
    def update_users(self,request,pk=None):
        user=self.queryset.get(pk=pk)
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user_serializer=self.get_serializer(user,data=request.data)
        if not user_serializer.is_valid():
            # user_serializer.save()
            return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        unit_serializer.save()
        return Response(status=status.HTTP_200_OK,data=user_serializer.data)

    @swagger_auto_schema(method="patch", request_body=UserSerializer)
    @action(detail=True, methods=["PATCH"])
    def activate(self,request,pk=None):
        print(request.data)
        user=None
        try:
            user = User.objects.get(pk=pk)
            print(user)
            user_serializer=UserSerializer(user,data=request.data,partial=True)
            print(user.birthdate)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(data=user_serializer.data)
           
            return Response(data=user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get_search_results(self, view, request):
        return Response("none")
