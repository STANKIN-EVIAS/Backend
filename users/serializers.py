from typing import Any
from rest_framework import serializers

from pets.serializers import PetSerializer
from .models import User
from django.contrib.auth import authenticate


class UserBriefSerializer(serializers.ModelSerializer):
    """Сериализатор для краткого представления пользователя."""

    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "full_name", "image"]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip() or obj.email


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода данных пользователя."""

    full_name = serializers.SerializerMethodField()
    pets_count = serializers.SerializerMethodField()
    pets = PetSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "phone_number",
            "role",
            "image",
            "pets_count",
            "pets",
        ]
        read_only_fields = ["id", "role"]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip() or obj.email

    def get_pets_count(self, obj):
        return obj.pets.count()
