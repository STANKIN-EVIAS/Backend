from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny

from pets.models import Pet
from pets.serializers import PetSerializer
from vet_clinics.models import Clinic, Service, Veterinarian
from vet_clinics.serializers import ClinicSerializer, ServiceSerializer, VeterinarianSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class VetClinicsViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer


class VeterinarianList(generics.ListAPIView):
    serializer_class = VeterinarianSerializer

    def get_queryset(self):
        clinic_id = self.kwargs.get("clinic_id")
        return Veterinarian.objects.filter(clinic_id=clinic_id)
