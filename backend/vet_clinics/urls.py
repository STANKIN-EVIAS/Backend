from django.urls import path, include
from .views import ServiceViewSet, VetClinicsViewSet, VeterinarianList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"services", ServiceViewSet, basename="Services")
router.register(r"", VetClinicsViewSet, basename="VetClinics")

urlpatterns = [
    # список питомцев конкретного пользователя
    path("<int:clinic_id>/veterinarians/", VeterinarianList.as_view(), name="clinic-veterinarians"),
    path("", include(router.urls)),
]
