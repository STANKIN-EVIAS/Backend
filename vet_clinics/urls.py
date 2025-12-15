from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AppointmentView, ServiceViewSet, TreatmentView, VetClinicsViewSet, VeterinarianList

router = DefaultRouter()
router.register(r"services", ServiceViewSet, basename="Services")
router.register(r"appointments", AppointmentView, basename="Appointments")
router.register(r"treatments", TreatmentView, basename="Treatments")
router.register(r"", VetClinicsViewSet, basename="VetClinics")

urlpatterns = [
    # список питомцев конкретного пользователя
    path("<int:clinic_id>/veterinarians/", VeterinarianList.as_view(), name="clinic-veterinarians"),
    path("", include(router.urls)),
]
