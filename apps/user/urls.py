from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.user.api import views


urlpatterns = [
    path("user/", views.index, name = "test user"),
]
