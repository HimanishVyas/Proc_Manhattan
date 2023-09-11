from django.urls import path
from package.api import views

from rest_framework.routers import DefaultRouter
from package.api import views

from package.api.views import (
    AddBusinessAPI,
    AddFrenchiesAPI
)

router = DefaultRouter()
router.register("add_business", AddBusinessAPI, basename="Add Business API")
router.register("add_frenchies", AddFrenchiesAPI, basename="Add Frenchies API")



urlpatterns = [
    # path("package/", views.view, name = "test"),
] + router.urls
