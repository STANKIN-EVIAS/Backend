from typing import Any
from django.views.generic import UpdateView
from rest_framework import serializers

from pets.serializers import PetSerializer
from .models import User
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
import logging

logger = logging.getLogger("evias")


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода данных пользователя."""

    pets = PetSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "phone_number", "role", "image", "pets"]
        read_only_fields = ["id"]


class RegisterSerializer(serializers.ModelSerializer):
    """Сериализатор регистрации. Создаёт пользователя с хешированным паролем."""

    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def create(self, validated_data):
        # Если username не передан, подставляем email.
        if not validated_data.get("username"):
            validated_data["username"] = validated_data.get("email")
        # create_user корректно захеширует пароль через UserManager
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    """Сериализатор логина. При успешной валидации возвращает JWT-токены."""

    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        # ModelBackend ожидает аргумент username. В нашей модели
        # USERNAME_FIELD = 'email', поэтому передаём email как username.
        user = authenticate(request=self.context.get("request"), username=email, password=password)
        if not user:
            raise serializers.ValidationError("Неверный email или пароль")

        from rest_framework_simplejwt.tokens import RefreshToken

        refresh = RefreshToken.for_user(user)
        attrs["access"] = str(refresh.access_token)
        attrs["refresh"] = str(refresh)

        return attrs
