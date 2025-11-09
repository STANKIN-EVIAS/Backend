from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnimalGenusViewSet, SpeciesViewSet, PetViewSet, UserPetsAPIView, UserPetsList


router = DefaultRouter()
router.register(r"genus", AnimalGenusViewSet, basename="genus")
router.register(r"species", SpeciesViewSet, basename="species")
router.register(r"", PetViewSet, basename="pet")

urlpatterns = [
    path("my/", UserPetsAPIView.as_view(), name="my-pets"),
    path("user/<int:user_id>/", UserPetsList.as_view(), name="user-pets"),
    path("", include(router.urls)),
]
