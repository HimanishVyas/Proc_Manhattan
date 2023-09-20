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
from package.utilities.create_package import create_package
from package.api.serializer import (
    AddBusinessSerializer,
    AddHallSerializer,
    AddCatressSerializer,
    # AddFrenchiesSerializer,
    # AddPackageSerializer,
    # ----------------------------------------------------------------------------------------------
    BusinessListSerializer,
    # FrenchiesListSerializer,
    HallListSerializer,
    CatressListSerializer,
    PackageListSerializer,
)

from package.models import (
    Business,
    # Frenchies,
    Package,
    Hall,
    Catress,
)


# Create your views here.

class AddBusinessAPI(CustomViewSet):
    serializer_class = BusinessListSerializer
    queryset = Business.objects.all()
    permission_classes = [IsVendor]

    def create(self, request):
        if request.user.user_role == 2:
            request.data["user_fk"] = request.user.id

        business_serializer = AddBusinessSerializer(data=request.data)
        if business_serializer.is_valid(raise_exception=True):
            business_serializer.save()
            response = {
                "message": "Business Registered",
                "status": status.HTTP_201_CREATED
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(business_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddHallAPI(CustomViewSet):
    serializer_class = HallListSerializer
    queryset = Hall.objects.all()
    permission_classes = [IsVendor]

    def create(self, request):
        data = request.data
        if request.user.user_role == 2:
            business = Business.objects.get(user_fk=request.user, business_type=1).id
            request.data['business_fk'] = business
        # ---->>package package_preference logic here
        if data["price_par_wedding"] <= 50000:
            request.data['package_preference'] = 3
        elif data["price_par_wedding"] <= 75000:
            request.data['package_preference'] = 2
        else:
            request.data['package_preference'] = 1

        hall_serializer = AddHallSerializer(data=request.data)
        if hall_serializer.is_valid(raise_exception=True):
            hall_serializer.save()

            # hall_id = Hall.objects.all().last().id
            hall = Hall.objects.all().last()
            create_package(hall)
            # create_package(hall=hall)

            response = {
                "message": "Hall Registered",
                "status": status.HTTP_201_CREATED
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(hall_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddCatressAPI(CustomViewSet):
    serializer_class = CatressListSerializer
    queryset = Catress.objects.all()
    permission_classes = [IsVendor]

    def create(self, request):
        data = request.data
        if request.user.user_role == 2:
            business = Business.objects.get(user_fk=request.user, business_type=2).id
            request.data['business_fk'] = business
        # ---->> total_price logic here
        data["total_price"] = (data["price_par_plate"] * data["capacity"]) + 35000

        # ---->>package package_preference logic here
        if data["total_price"] <= 100000:
            request.data['package_preference'] = 3
        elif data["total_price"] <= 200000:
            request.data['package_preference'] = 2
        else:
            request.data['package_preference'] = 1

        catress_serializer = AddCatressSerializer(data=request.data)
        if catress_serializer.is_valid(raise_exception=True):
            catress_serializer.save()
            response = {
                "message": "Catress Registered",
                "status": status.HTTP_201_CREATED
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(catress_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PackageListAPI(CustomViewSet):
    serializer_class = PackageListSerializer
    queryset = Package.objects.all()
    permission_classes = [IsCustomer]
