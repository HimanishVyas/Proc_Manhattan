from django.contrib import admin
from django.apps import apps
# Register your models here.

from .models import User

# models = apps.get_app_config("user").get_models()
# for model in models:
#     admin.site.register(model)

admin.site.register(User)
