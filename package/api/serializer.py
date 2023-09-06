from django.utils.encoding import DjangoUnicodeDecodeError, force_bytes, smart_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from dotenv import load_dotenv

# from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from package.models import (
    Business
)

class AddBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = "__all__"
