import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny

from pets.models import Pet
from pets.models import UserPet
from pets.serializers import PetSerializer


# Create your views here.
class PetsViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    # permission_classes = [IsAuthenticated]  # доступ только авторизованным


class UserPetsList(generics.ListAPIView):
    """Возвращает список питомцев для указанного пользователя (user_id)."""

    serializer_class = PetSerializer

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Pet.objects.filter(userpet__user_id=user_id)


class UserPetsAPIView(generics.ListAPIView):
    """
    API: Список питомцев пользователя
    """

    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        return Pet.objects.filter(userpet__user_id=user_id)

    def get(self, request, *args, **kwargs):
        """Возврат профиля в формате JSON."""
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
