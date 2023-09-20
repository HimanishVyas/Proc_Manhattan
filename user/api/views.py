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
    AddAddressSerializer,
    CountrySerializer,
    StateSerializer,
    DistrictSerializer,
    ChangePasswordSerializer,
)

from user.models import (
    User,
    Address,
    Country,
    State,
    District

)

# Create your views here.

# -------------SignUpApi-------------

class SignUpApi(ViewSet):
    authentication_classes = []

    def create(self, request):
        serializer = UserRegisterSerializer(
            data=request.data, context={"host": request.META["HTTP_HOST"]}
        )
        if serializer.is_valid():
            user = serializer.save()
            response = {
                "message": "user created , Please check your email and mobile for verification",
                "user_id": user.id,
                "user_name": user.name,
                "user_phone": str(user.mobile),
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
                if not user.email_verify:
                    return Response(
                        {"msg": "Email is not verified"}, status=status.HTTP_200_OK
                    )
                user_serializer = UserDepthSerializer(user)
                user.save()
                token = get_tokens_for_user(user)
                response = user_serializer.data
                response["token"] = token
                response = {"data": response, "status": status.HTTP_200_OK}
                return Response(response, status=status.HTTP_200_OK)
            return Response(
            {
                "message": "Invalid Email or Password HAHA",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

# -------------ChangePasswordApi-------------


class ChangePasswordApi(ViewSet):

    def create(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data, context={"user_email": request.user.email}
        )
        if serializer.is_valid():
            return Response(
                {"message": "password changed succesfully"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": "Somthig went wrong"}, status=status.HTTP_403_FORBIDDEN
            )



class AddAddressApi(CustomViewSet):
    serializer_class = AddAddressSerializer
    queryset = Address.objects.all()
    
class CountryApi(CustomViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    
class DistrictApi(CustomViewSet):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()

class StateApi(CustomViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()
    
