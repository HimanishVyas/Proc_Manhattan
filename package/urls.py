from django.urls import path
from package.api import views


urlpatterns = [
    path("package/", views.view, name = "test"),
]
