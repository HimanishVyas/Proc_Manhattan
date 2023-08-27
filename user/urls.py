from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.api import views

from user.api.views import (
    SignUpApi,
    LoginApi,
    UserListApi,
    AddAddressApi,
    StateApi,
    DistrictApi,
    CountryApi
)

router = DefaultRouter()
router.register("signup", SignUpApi, basename="Sign Up API")
router.register("login", LoginApi, basename="Login API")
router.register("user_list", UserListApi, basename="Customer list Api")
router.register("address", AddAddressApi, basename="Add Address Api")
router.register("state", StateApi, basename="state Api")
router.register("country", CountryApi, basename="country Api")
router.register("district", DistrictApi, basename="district Api")



urlpatterns = [
    # path("user/", views.index, name = "test user"),
] + router.urls
