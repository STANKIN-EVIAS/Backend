from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()


router.register(r"passports", views.PassportViewSet, basename="passport")
router.register(r"certificates", views.CertificateViewSet, basename="certificate")
router.register(r"medical-cards", views.MedicalCardViewSet, basename="medical-card")
router.register(r"pet-documents", views.PetDocumentsView, basename="pet-documents")

urlpatterns = [
    path("", include(router.urls)),
]
