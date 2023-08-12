from django.urls import path
from apps.package.api import views


urlpatterns = [
    path("package/", views.view, name = "test"),
]
