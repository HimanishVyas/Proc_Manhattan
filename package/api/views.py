from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.sessions.backends.db import SessionStore
from phonenumber_field.phonenumber import PhoneNumber as pn
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from package.customs.viewsets import CustomViewSet
from package.customs.permissions import (
    IsCustomer, 
    IsVendor
)

from package.api.serializer import (
    AddBusinessSerializer,
)

from package.models import (
    Business,
)

# Create your views here.

class AddBusinessAPI(CustomViewSet):
    queryset = Business.objects.all()
    serializer_class = AddBusinessSerializer
    permission_classes = [IsVendor]
        
    def create(self, request):
        print("--------------------", request.user.user_role)
        if request.user.user_role == 2:
            request.data["user_fk"] = request.user.id

        business_serializer = AddBusinessSerializer(data=request.data)
        if business_serializer.is_valid(raise_exception=True):
            business_serializer.save()
            response = {
                "message" : "Business Ragisterd",
                "status" : status.HTTP_201_CREATED
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(business_serializer.errors, status=status.HTTP_400_BAD_REQUEST)