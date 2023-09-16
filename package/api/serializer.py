from django.utils.encoding import DjangoUnicodeDecodeError, force_bytes, smart_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from dotenv import load_dotenv

# from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from package.models import (
    Business,
    # Frenchies,
    Package,
    Hall,
    Catress
)


# _________addition Serializers_________
class AddBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = "__all__"


class AddHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = "__all__"


class AddCatressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catress
        fields = "__all__"


# class AddFrenchiesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Frenchies
#         fields = "__all__"'

# class AddPackageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Frenchies
#         fields = "__all__"

# _________List Serializers_________

# class FrenchiesListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Frenchies
#         fields = "__all__"
#         depth = 1

class BusinessListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = "__all__"
        depth = 1


class HallListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = "__all__"
        depth = 1


class CatressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catress
        fields = "__all__"
        depth = 1


class PackageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = "__all__"
        depth = 1
