from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.api import views

from user.api.views import (
    SignUpApi,
)

router = DefaultRouter()
router.register("signup", SignUpApi, basename="Sign Up API")

urlpatterns = [
    # path("user/", views.index, name = "test user"),
] + router.urls
