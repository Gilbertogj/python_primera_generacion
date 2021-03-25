from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .models import PetOwner, Pet
from .forms import OwnerForm

# Create your views here.
# def list_pet_owners(request):
#     """List owners."""
#     owners = PetOwner.objects.all()
#     context = {"owners": owners}

#     template = loader.get_template("vet/owners/list.html")
#     return HttpResponse(template.render(context, request))

# class Owners(View):
#     def get(self, request):
#         owners = PetOwner.objects.all()
#         context = {"owners": owners}

#         template = loader.get_template("vet/owners/list.html")
#         return HttpResponse(template.render(context, request))

# class OwnersList(TemplateView):
#     template_name = "vet/owners/list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(context, "ESTO VIENE DEL PADRE (TEMPLATEVIEW)")
#         context["owners"] = PetOwner.objects.all()
#         print(context, "ESTO LE AGREGAMOS NOSOTROS")
#         return context

class OwnersList(ListView):
    model = PetOwner
    template_name = "vet/owners/list.html"
    context_object_name = "owners"

class OwnersDetail(DetailView):
    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = "owner"

class OwnersCreate(CreateView):
    model = PetOwner
    template_name = "vet/owners/create.html"
    form_class = OwnerForm
    success_url = reverse_lazy("vet:owners_list")

class PetsList(ListView):
    model = Pet
    template_name = "vet/pets/list.html"
    context_object_name = "pets"

class PetsDetail(DetailView):
    model = Pet
    template_name = "vet/pets/detail.html"
    context_object_name = "pet"