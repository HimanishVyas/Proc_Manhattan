from django.urls import path
from package.api import views

from rest_framework.routers import DefaultRouter
from package.api import views

from package.api.views import (
    AddBusinessAPI,
    PackageListAPI,
    AddHallAPI,
    AddCatressAPI,
)

router = DefaultRouter()
router.register("add_business", AddBusinessAPI, basename="Add Business API")
router.register("add_hall", AddHallAPI, basename="Add Hall API")
router.register("add_catress", AddCatressAPI, basename="Add Catress API")
router.register("package_list", PackageListAPI, basename="Package List API")


urlpatterns = [
    # path("package/", views.view, name = "test"),
] + router.urls
