from django.urls import path

from .views import Owners

urlpatterns = [
    path("owners/", Owners.as_view())
    ]