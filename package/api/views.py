from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.sessions.backends.db import SessionStore
from phonenumber_field.phonenumber import PhoneNumber as pn
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from package.customs.viewsets import CustomViewSet


# Create your views here.

class AddBusinessAPI(CustomViewSet):
    
    def create(self, request):
        pass