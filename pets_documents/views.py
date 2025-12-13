from django.db.models import Q
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from pets.models import Pet

from .models import Certificate, MedicalCard, Passport
from .serializers import CertificateSerializer, MedicalCardSerializer, PassportSerializer, PetDocumentsSerializer


class PassportViewSet(viewsets.ModelViewSet):
    """ViewSet для паспортов питомцев"""

    queryset = Passport.objects.all()
    serializer_class = PassportSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["passport_number", "pet__name", "microchip_number"]
    filterset_fields = ["pet", "country_of_issue"]
    ordering_fields = ["issue_date", "passport_number"]

    def get_queryset(self):
        """Фильтрация по текущему пользователю"""
        queryset = super().get_queryset()

        # Если пользователь не админ, показываем только его питомцев
        if not self.request.user.is_staff:
            queryset = queryset.filter(pet__owner=self.request.user)

        return queryset

    @action(detail=False, methods=["get"], url_path="pet/(?P<pet_id>\d+)")
    def get_by_pet(self, request, pet_id=None):
        """Получить паспорт конкретного питомца"""
        # Проверяем, что питомец принадлежит пользователю
        if not request.user.is_staff:
            pet = get_object_or_404(Pet, id=pet_id, owner=request.user)
        else:
            pet = get_object_or_404(Pet, id=pet_id)

        passport = get_object_or_404(Passport, pet=pet)
        serializer = self.get_serializer(passport)
        return Response(serializer.data)


class CertificateViewSet(viewsets.ModelViewSet):
    """ViewSet для сертификатов"""

    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["certificate_number", "title", "pet__name", "issued_by"]
    filterset_fields = ["pet", "certificate_type"]
    ordering_fields = ["issue_date", "expiration_date"]

    def get_queryset(self):
        """Фильтрация по текущему пользователю"""
        queryset = super().get_queryset()

        # Если пользователь не админ, показываем только его питомцев
        if not self.request.user.is_staff:
            queryset = queryset.filter(pet__owner=self.request.user)

        # Фильтр по типу сертификата через query params
        certificate_type = self.request.query_params.get("type", None)
        if certificate_type:
            queryset = queryset.filter(certificate_type=certificate_type)

        # Фильтр по наличию даты истечения
        show_expired = self.request.query_params.get("show_expired", None)
        if show_expired == "true":
            # Показать все
            pass
        elif show_expired == "only":
            # Только просроченные
            from django.utils import timezone

            queryset = queryset.filter(expiration_date__lt=timezone.now().date())
        elif show_expired == "active":
            # Только активные (не просроченные)
            from django.utils import timezone

            queryset = queryset.filter(Q(expiration_date__gte=timezone.now().date()) | Q(expiration_date__isnull=True))

        return queryset

    @action(detail=False, methods=["get"], url_path="pet/(?P<pet_id>\d+)")
    def get_by_pet(self, request, pet_id=None):
        """Получить все сертификаты конкретного питомца"""
        # Проверяем, что питомец принадлежит пользователю
        if not request.user.is_staff:
            pet = get_object_or_404(Pet, id=pet_id, owner=request.user)
        else:
            pet = get_object_or_404(Pet, id=pet_id)

        certificates = Certificate.objects.filter(pet=pet)
        serializer = self.get_serializer(certificates, many=True)
        return Response(serializer.data)


class MedicalCardViewSet(viewsets.ModelViewSet):
    """ViewSet для медицинских карт"""

    queryset = MedicalCard.objects.all()
    serializer_class = MedicalCardSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["medical_number", "pet__name", "blood_type"]
    filterset_fields = ["pet"]

    def get_queryset(self):
        """Фильтрация по текущему пользователю"""
        queryset = super().get_queryset()

        # Если пользователь не админ, показываем только его питомцев
        if not self.request.user.is_staff:
            queryset = queryset.filter(pet__owner=self.request.user)

        return queryset

    @action(detail=False, methods=["get"], url_path="pet/(?P<pet_id>\d+)")
    def get_by_pet(self, request, pet_id=None):
        """Получить медицинские карты конкретного питомца"""
        # Проверяем, что питомец принадлежит пользователю
        if not request.user.is_staff:
            pet = get_object_or_404(Pet, id=pet_id, owner=request.user)
        else:
            pet = get_object_or_404(Pet, id=pet_id)

        medical_cards = MedicalCard.objects.filter(pet=pet)
        serializer = self.get_serializer(medical_cards, many=True)
        return Response(serializer.data)


# Дополнительные представления для удобства
class PetDocumentsView(viewsets.GenericViewSet):
    """Представление для получения всех документов питомца"""

    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"], url_path="(?P<pet_id>\d+)/all")
    def get_all_documents(self, request, pet_id=None):
        """Получить все документы питомца одним запросом"""
        # Проверяем, что питомец принадлежит пользователю
        if not request.user.is_staff:
            pet = get_object_or_404(Pet, id=pet_id, owner=request.user)
        else:
            pet = get_object_or_404(Pet, id=pet_id)

        data = {
            "passport": Passport.objects.filter(pet=pet).first(),
            "certificates": Certificate.objects.filter(pet=pet),
            "medical_cards": MedicalCard.objects.filter(pet=pet),
        }

        serializer = PetDocumentsSerializer(data)
        return Response(serializer.data)
