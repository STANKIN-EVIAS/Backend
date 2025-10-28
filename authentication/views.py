from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import LoginSerializer, RegistrationSerializer


class RegistrationView(generics.CreateAPIView):
    """Эндпоинт регистрации. При успешной регистрации возвращает access и refresh токены."""

    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        data = serializer.data
        data["access"] = str(refresh.access_token)
        data["refresh"] = str(refresh)

        return Response(data, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    """Эндпоинт логина. При успешной валидации возвращает access и refresh токены."""

    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
