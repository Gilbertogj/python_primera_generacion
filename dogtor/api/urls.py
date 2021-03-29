from django.urls import path, include
# from rest_framework import routers
# from .views import OwnersViewSet, PetsViewSet, DatesViewSet

from .views import (ListOwnersAPIView, RetrieveOwnersAPIView, CreateOwnersAPIView, ListPetsAPIView,
CreatePetsAPIView, RetrievePetsAPIView, UpdateOwnersAPIView, 
UpdatePetsAPIView, DestroyOwnersAPIView, DestroyPetsAPIView, 
RetrieveOwnerPetsAPIView, RetrievePetsOwnerAPIView, ListOfficesAPIView, CreateOfficesAPIView,
RetrieveOfficesAPIView, CreateDatesAPIView
)

urlpatterns =[
    path("owners/", ListOwnersAPIView.as_view(), name="list-owners"),
    path("owners/create", CreateOwnersAPIView.as_view(), name="create-owners"),
    path("owners/<int:pk>/", RetrieveOwnersAPIView.as_view(),name="retrieve-owners"),
    path("owners/update/<int:pk>/", UpdateOwnersAPIView.as_view(),name="update-owners"),
    path("owners/destroy/<int:pk>/", DestroyOwnersAPIView.as_view(),name="destroy-owners"),
    path(
        "owners/<int:pk>/pets/",
        RetrieveOwnerPetsAPIView.as_view(),
        name="retrieve-owner-pets",
    ),
    path("pets/", ListPetsAPIView.as_view(), name="list-petds"),
    path("pets/create", CreatePetsAPIView.as_view(), name="create-pets"),
    path("pets/<int:pk>/", RetrievePetsAPIView.as_view(),name="retrieve-pets"),
    path("pets/update/<int:pk>/", UpdatePetsAPIView.as_view(),name="update-pets"),
    path("pets/destroy/<int:pk>/", DestroyPetsAPIView.as_view(),name="destroy-pets"),
    path(
        "pets/<int:pk>/", RetrievePetsOwnerAPIView.as_view(), name="retrieve-pets-owner"
    ),
    path("offices/", ListOfficesAPIView.as_view(), name="list-offices"),
    path("offices/create", CreateOfficesAPIView.as_view(), name="create-offices"),

    path("offices/<int:pk>/", RetrieveOfficesAPIView.as_view(), name="retrive-offices"),

    path("dates/create", CreateDatesAPIView.as_view(), name="create-dates"),
    





]


# router = routers.DefaultRouter()
# router.register(r"owners",OwnersViewSet)
# router.register(r"pets",PetsViewSet)
# router.register(r"dates",DatesViewSet)

# urlpatterns = [
#     path("", include(router.urls)),
# ]
