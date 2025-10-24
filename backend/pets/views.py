from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied

from .models import AnimalGenus, Species, Pet, UserPet
from .serializers import AnimalGenusSerializer, SpeciesSerializer, PetSerializer, PetDetailSerializer, UserPetSerializer


class AnimalGenusViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для просмотра родов животных."""

    queryset = AnimalGenus.objects.all()
    serializer_class = AnimalGenusSerializer
    permission_classes = [AllowAny]


class SpeciesViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для просмотра пород животных."""

    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Species.objects.all()
        genus_id = self.request.query_params.get("genus", None)
        if genus_id is not None:
            queryset = queryset.filter(category_id=genus_id)
        return queryset


class PetViewSet(viewsets.ModelViewSet):
    """
    ViewSet для полного управления питомцами.

    Предоставляет стандартные CRUD операции и дополнительные действия
    для управления владельцами питомцев.

    Методы:
    - GET /pets/ - получение списка всех питомцев
    - POST /pets/ - создание нового питомца
    - GET /pets/{id}/ - получение информации о конкретном питомце
    - PUT/PATCH /pets/{id}/ - обновление информации о питомце
    - DELETE /pets/{id}/ - удаление питомца
    - POST /pets/{id}/add_owner/ - добавление нового владельца
    - POST /pets/{id}/remove_owner/ - удаление владельца

    Права доступа:
    - Просмотр: авторизованные пользователи
    - Создание: авторизованные пользователи
    - Редактирование: владельцы питомца
    - Удаление: владельцы питомца
    - Управление владельцами: текущие владельцы питомца
    """

    queryset = Pet.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """
        Возвращает подходящий сериализатор в зависимости от действия.
        Для детального просмотра используется расширенный сериализатор.
        """
        if self.action == "retrieve":
            return PetDetailSerializer
        return PetSerializer

    def perform_create(self, serializer):
        """
        При создании питомца автоматически назначает текущего пользователя
        владельцем через промежуточную модель UserPet.
        """
        pet = serializer.save()
        UserPet.objects.create(user=self.request.user, pet=pet)

    @action(detail=True, methods=["post"])
    def add_owner(self, request, pk=None):
        """
        Добавляет нового владельца питомцу.

        Требует передачи user_id в теле запроса.
        Только текущие владельцы могут добавлять новых.

        Returns:
            200: {"status": "owner added"} - владелец успешно добавлен
            400: {"error": "user_id required"} - не указан ID пользователя
            403: Forbidden - нет прав на добавление владельцев
        """
        pet = self.get_object()
        if request.user not in pet.owners.all():
            raise PermissionDenied("У вас нет прав на добавление владельцев этому питомцу")

        user_id = request.data.get("user_id")
        if user_id:
            UserPet.objects.create(user_id=user_id, pet=pet)
            return Response({"status": "owner added"})
        return Response({"error": "user_id required"}, status=400)

    @action(detail=True, methods=["post"])
    def remove_owner(self, request, pk=None):
        """
        Удаляет владельца у питомца.

        Требует передачи user_id в теле запроса.
        Только текущие владельцы могут удалять других владельцев.

        Returns:
            200: {"status": "owner removed"} - владелец успешно удален
            400: {"error": "user_id required"} - не указан ID пользователя
            403: Forbidden - нет прав на удаление владельцев
        """
        pet = self.get_object()
        if request.user not in pet.owners.all():
            raise PermissionDenied("У вас нет прав на удаление владельцев этого питомца")

        user_id = request.data.get("user_id")
        if user_id:
            UserPet.objects.filter(user_id=user_id, pet=pet).delete()
            return Response({"status": "owner removed"})
        return Response({"error": "user_id required"}, status=400)


class UserPetsList(generics.ListAPIView):
    """Возвращает список питомцев для указанного пользователя."""

    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Pet.objects.filter(userpet__user_id=user_id)


class UserPetsAPIView(generics.ListCreateAPIView):
    """API для работы со списком питомцев текущего пользователя."""

    serializer_class = UserPetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserPet.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
