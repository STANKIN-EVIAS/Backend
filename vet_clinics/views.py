from rest_framework import generics, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny, IsAuthenticated

from vet_clinics.models import Appointment, Clinic, Service, Treatment, Veterinarian
from vet_clinics.serializers import (
    AppointmentSerializer,
    ClinicSerializer,
    ServiceSerializer,
    TreatmentSerializer,
    VeterinarianSerializer,
)


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


class AppointmentView(viewsets.ModelViewSet):
    """CRUD для записей на приём. Пользователи видят только свои записи, staff видит все."""

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Appointment.objects.all()
        user = self.request.user

        if not user.is_staff:
            qs = qs.filter(user=user)

        clinic_id = self.request.query_params.get("clinic_id")
        if clinic_id:
            qs = qs.filter(clinic_id=clinic_id)
        return qs

    def perform_create(self, serializer):
        pet = serializer.validated_data.get("pet")
        if not self.request.user.is_staff:
            if self.request.user not in pet.owners.all():
                raise PermissionDenied("У вас нет прав создавать запись для этого питомца")
        serializer.save(user=self.request.user)


class TreatmentView(viewsets.ModelViewSet):
    """CRUD для лечебных процедур.

    Ветеринары видят свои процедуры, владельцы — процедуры по своим питомцам, staff видит всё.
    При создании, если пользователь — ветеринар, он будет подставлен автоматически.
    """

    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Treatment.objects.all()

        vet_profile = getattr(user, "veterinarian_profile", None)
        if vet_profile:
            return Treatment.objects.filter(veterinarian=vet_profile)

        return Treatment.objects.filter(pet__owners=user)

    def perform_create(self, serializer):
        user = self.request.user
        vet_profile = getattr(user, "veterinarian_profile", None)
        pet = serializer.validated_data.get("pet")

        if vet_profile:
            serializer.save(veterinarian=vet_profile)
            return

        # обычный пользователь — проверяем права на питомца
        if not user.is_staff and user not in pet.owners.all():
            raise PermissionDenied("У вас нет прав создавать лечение для этого питомца")
        serializer.save()
