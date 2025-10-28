from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


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
        user = authenticate(
            request=self.context.get("request"), username=email, password=password
        )
        if not user:
            raise serializers.ValidationError("Неверный email или пароль")

        refresh = RefreshToken.for_user(user)
        attrs["access"] = str(refresh.access_token)
        attrs["refresh"] = str(refresh)

        return attrs


class RegistrationSerializer(serializers.ModelSerializer):
    """Сериализатор регистрации. Создаёт пользователя с хешированным паролем."""

    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True, min_length=6)
    password2 = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]

    def validate(self, attrs):
        """Проверяем совпадение паролей перед созданием."""
        if attrs.get("password1") != attrs.get("password2"):
            raise serializers.ValidationError({"password2": "Пароли не совпадают."})
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password1")

        # Если username не передан, подставляем email до '@'
        if not validated_data.get("username"):
            validated_data["username"] = validated_data.get("email").split("@")[0]

        user = User.objects.create_user(**validated_data, password=password)
        return user
