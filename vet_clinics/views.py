from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from vet_clinics.models import Clinic, Service, Veterinarian
from vet_clinics.serializers import ClinicSerializer, ServiceSerializer, VeterinarianSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]


class VetClinicsViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    permission_classes = [AllowAny]


class VeterinarianList(generics.ListAPIView):
    serializer_class = VeterinarianSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        clinic_id = self.kwargs.get("clinic_id")
        return Veterinarian.objects.filter(clinic_id=clinic_id)
