from django.contrib.auth import authenticate
from django.contrib.sessions.backends.db import SessionStore
from phonenumber_field.phonenumber import PhoneNumber as pn
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from user.customs.permissions import ExceptDelete, ReadOnly
from user.customs.viewsets import CustomViewSet

from user.utilities.utils import (
    get_tokens_for_user,
)

from user.api.serializer import (
    UserRegisterSerializer,
    UserListSerializer,
    LoginSerializer,
    UserDepthSerializer,
)

from user.models import (
    User,
)

# Create your views here.

# -------------SignUpApi-------------

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

# -------------CustomerUSerApi-------------

class UserListApi(CustomViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = [ReadOnly]


# -------------LoginApi-------------


class LoginApi(ViewSet):
    authentication_classes = []


    def create(self, request):

        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.validated_data["password"]
            # password = serializer.data.get('password')
            user = User.objects.filter(email=email).first()            
            user = authenticate(email=email, password=password)
            # logging.info("Login created.")
            if user:
                # if not user.mobile_verify:
                #     return Response(
                #         {"msg": "mobile number is not verified"},
                #         status=status.HTTP_200_OK,
                #     )
                # if not user.email_verify:
                #     return Response(
                #         {"msg": "Email is not verified"}, status=status.HTTP_200_OK
                #     )
                user_serializer = UserDepthSerializer(user)
                # user.fcm_token = serializer.validated_data["fcm_token"]
                user.save()
                token = get_tokens_for_user(user)
                response = user_serializer.data
                response["token"] = token
                response = {"data": response, "status": status.HTTP_200_OK}
                # logging.info("User created successfully")
                return Response(response, status=status.HTTP_200_OK)
            return Response(
            {
                "message": "Invalid Email or Password HAHA",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )




        # serializer = LoginSerializer(data=request.data)
        # if serializer.is_valid():
        #     email = serializer.validated_data["email"]
        #     print("----------->>>>", email)
        #     password = serializer.validated_data["password"]
        #     print("----------->>>>", password)
        #     user = authenticate(email=email, password=password)
        #     print("----------->>>>", user)
        #     if user:
        #         # if not user.mobile_verify:
        #         #     return Response(
        #         #         {"message": "mobile number is not verified"},
        #         #         status=status.HTTP_200_OK,
        #         #    )
        #         if not user.email_verify:
        #             return Response(
        #                 {"message": "Email is not verified"}, status=status.HTTP_200_OK
        #             )
        #         user_serializer = UserDepthSerializer(user, context={"request": request})
        #         if request.data.get("fcm_token"):
        #             user.fcm_token = request.data.get("fcm_token")
        #             user.save()
        #         token = get_tokens_for_user(user)
        #         response = user_serializer.data
        #         response["token"] = token
        #         return Response(response, status=status.HTTP_200_OK)
        #     return Response(
        #         {"message": "Invalid Email or Password"},
        #         status=status.HTTP_400_BAD_REQUEST,
        #     )
        # else:
        #     return Response({"error":"invalid data"}, status=status.HTTP_400_BAD_REQUEST)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# ________test___change_____