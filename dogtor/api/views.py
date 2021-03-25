from rest_framework import viewsets

from vet.models import PetOwner, Pet, PetDate
from .serializers import OwnersSerializer, PetsSerializer, DatesSerializer

# Create your views here.
class OwnersViewSet(viewsets.ModelViewSet):
    """
    ViewSet del modelo PetOwners.
    """

    queryset= PetOwner.objects.all()
    serializer_class = OwnersSerializer

class PetsViewSet(viewsets.ModelViewSet):
    """
    ViewSet del modelo Pets.
    """

    queryset= Pet.objects.all()
    serializer_class = PetsSerializer

class DatesViewSet(viewsets.ModelViewSet):
    """
    ViewSet del modelo PetDate.
    """

    queryset= PetDate.objects.all()
    serializer_class = DatesSerializer


