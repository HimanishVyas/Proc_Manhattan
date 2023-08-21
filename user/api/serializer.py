import os

from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator

# from django.contrib.sessions.backends.db import SessionStore
from django.utils.encoding import DjangoUnicodeDecodeError, force_bytes, smart_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from dotenv import load_dotenv

# from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

# from apps.user.customs.authentications import decode_access_token
from user.models import (
    User,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def get_user_image(self, user):
        request = self.context.get("request")
        photo_url = user.user_image.url
        return request.build_absolute_uri(photo_url)

    def create(self, validated_data):
        return super().create(validated_data)


class UserDepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        depth = 1


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField()

    class Meta:
        model = User
        fields = [
            "name",
            "email",
            "password",
            "confirm_password",
            "user_role",
            "mobile",
        ]

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        if password != confirm_password:
            raise serializers.ValidationError(
                {"Error": "Passwords and confirm passwords are not match"}
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = super().create(validated_data)
        print("user-------->>>>", user)
        user = User.objects.filter(id=user.id).first()
        # id = urlsafe_base64_encode(force_bytes(user.id))
        # token = PasswordResetTokenGenerator().make_token(user)
        # host = self.context.get("host")
        # link = f"http://{host}/verify_link/" + id + "/" + token + "/"
        # data = {
        #     "subject": "Account verification",
        #     "body": f"click Following Link for verified your Account {link}",
        #     "to_email": user.email,
        # }
        # Util.send_email(data)
        # # send_otp_via_phone(user.phone)
        # print("-------------------------")
        return user


class LoginSerializer(serializers.Serializer):
    # email = serializers.EmailField(allow_null=True)
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password", "placeholder": "Password"},
    )
    
    class Meta:
        fields = ('password', 'email',)

    # email = serializers.EmailField(max_length=50)

    # class Meta:
    #     model = User
    #     fields = ('email', 'password',)
    #     extra_kwargs = {
    #         'password': {'write_only': True}
    #     }


