from rest_framework import generics

from vet.models import PetOwner, Pet, PetDate, BranchOffice
from .serializers import (OwnersListSerializer, OwnersSerializer, PetsListSerializer, 
PetsSerializer, OwnerPetsSerializer, PetOwnerSerializer, OfficesListSerializer, 
OfficesSerializer, PetDatesSerializer, DateOfficesSerializer
)
# from .serializers import OwnersSerializer, PetsSerializer, DatesSerializer

#Vistas genericas

class ListOwnersAPIView(generics.ListAPIView):
    queryset = PetOwner.objects.all().order_by("created_at")
    serializer_class = OwnersListSerializer

class CreateOwnersAPIView(generics.CreateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class RetrieveOwnersAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class UpdateOwnersAPIView(generics.UpdateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class DestroyOwnersAPIView(generics.DestroyAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class ListPetsAPIView(generics.ListAPIView):
    queryset = Pet.objects.all().order_by("created_at")
    serializer_class = PetsListSerializer

class CreatePetsAPIView(generics.CreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

class RetrievePetsAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

class UpdatePetsAPIView(generics.UpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

class DestroyPetsAPIView(generics.DestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

class RetrieveOwnerPetsAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnerPetsSerializer

class RetrievePetsOwnerAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetOwnerSerializer


class ListOfficesAPIView(generics.ListAPIView):
    queryset = BranchOffice.objects.all()
    serializer_class = OfficesListSerializer

class CreateOfficesAPIView(generics.CreateAPIView):
    queryset = BranchOffice.objects.all()
    serializer_class = OfficesSerializer



class CreateDatesAPIView(generics.CreateAPIView):
    queryset = PetDate.objects.all()
    serializer_class = PetDatesSerializer

class RetrieveOfficesAPIView(generics.RetrieveAPIView):
    queryset = BranchOffice.objects.all()
    serializer_class = DateOfficesSerializer



# Create your views here.
# class OwnersViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet del modelo PetOwners.
#     """

#     queryset= PetOwner.objects.all()
#     serializer_class = OwnersSerializer

# class PetsViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet del modelo Pets.
#     """

#     queryset= Pet.objects.all()
#     serializer_class = PetsSerializer

# class DatesViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet del modelo PetDate.
#     """

#     queryset= PetDate.objects.all()
#     serializer_class = DatesSerializer


