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
    BusinessListSerializer,
    AddFrenchiesSerializer,
    FrenchiesListSerializer,
    AddPackageSerializer,

)

from package.models import (
    Business,
    Frenchies,
    Package
)

# Create your views here.

class AddBusinessAPI(CustomViewSet):
    serializer_class = BusinessListSerializer
    queryset = Business.objects.all()
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

    # def list(self, request):


class AddFrenchiesAPI(CustomViewSet):
    serializer_class = FrenchiesListSerializer
    queryset = Frenchies.objects.all()
    permission_classes = [IsVendor]

    def create(self, request):
        if request.user.user_role == 2:
            business = Business.objects.get(user_fk = request.user).id
            request.data['business_fk'] = business

        frenchies_serializer = AddFrenchiesSerializer(data=request.data)
        if frenchies_serializer.is_valid(raise_exception=True):
            frenchies_serializer.save()
            response = {
                "message": "Business Ragisterd",
                "status": status.HTTP_201_CREATED
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(frenchies_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AddPackageAPI(CustomViewSet):
    serializer_class = AddPackageSerializer
    queryset = Package.objects.all()

    # def create(self, request):