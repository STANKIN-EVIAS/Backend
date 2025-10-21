from django.urls import path, include
from .views import UserPetsAPIView, UserPetsList, PetsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", PetsViewSet, basename="pet")

urlpatterns = [
    # список питомцев конкретного пользователя
    path("profiles/", UserPetsAPIView.as_view(), name="pets-profiles"),
    path("user/<int:user_id>/", UserPetsList.as_view(), name="user-pets"),
    path("", include(router.urls)),
]
