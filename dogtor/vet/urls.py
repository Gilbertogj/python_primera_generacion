from django.urls import path

from .views import Owners, OwnersList, OwnersDetail

urlpatterns = [
    path("owners/", OwnersList.as_view()),
    path("owners/<int:pk>/", OwnersDetail.as_view()),
    ]