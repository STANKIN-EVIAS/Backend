from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from .models import User
import logging

logger = logging.getLogger("evias")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',"first_name","last_name", 'email', 'phone_number', 'role', 'image', 'pets']
        read_only_fields = ['id']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        # Ensure username is set (UserManager.create_user may require it)
        if not validated_data.get('username'):
            validated_data['username'] = validated_data.get('email')
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        # ModelBackend expects the username kwarg. Our User model sets
        # USERNAME_FIELD = 'email', so pass the email as 'username'.
        user = authenticate(request=self.context.get('request'), username=email, password=password)
        if not user:
            raise serializers.ValidationError('Неверный email или пароль')

        from rest_framework_simplejwt.tokens import RefreshToken
        refresh = RefreshToken.for_user(user)
        attrs['access'] = str(refresh.access_token)
        attrs['refresh'] = str(refresh)
        return attrs
