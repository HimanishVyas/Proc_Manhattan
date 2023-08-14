from django.contrib.auth import authenticate
from django.contrib.sessions.backends.db import SessionStore
from phonenumber_field.phonenumber import PhoneNumber as pn
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from user.api.serializer import (
    UserRegisterSerializer,
)

# Create your views here.

class SignUpApi(ViewSet):
    authentication_classes = []

    def create(self, request):
        print("-------------hello-------------")
        serializer = UserRegisterSerializer(
            data=request.data, context={"host": request.META["HTTP_HOST"]}
            # data=request.data

        )
        if serializer.is_valid():
            user = serializer.save()
            response = {
                "message": "user created , Please check your email and mobile for verification",
                "user_id": user.id,
                "user_name": user.name,
                # "user_phone": str(user.phone),
                "user_email": user.email,
                "status": status.HTTP_201_CREATED,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )
