from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, LoginSerializer
from pets.serializers import PetSerializer

class UserViewSet(viewsets.ModelViewSet):
    """Стандартный ViewSet для управления пользователями (CRUD)."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]  # доступ только авторизованным


class RegisterView(generics.CreateAPIView):
    """Эндпоинт регистрации. При успешной регистрации возвращает JWT-токены."""
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()


        from rest_framework_simplejwt.tokens import RefreshToken
        refresh = RefreshToken.for_user(user)

        data = serializer.data
        data['access'] = str(refresh.access_token)
        data['refresh'] = str(refresh)

        return Response(data, status=status.HTTP_201_CREATED)



class LoginView(generics.GenericAPIView):
    """Эндпоинт логина. При успешной валидации возвращает access и refresh."""
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    """
    API: Профиль текущего пользователя.
    GET — получить профиль
    PUT/PATCH — обновить профиль
    """
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

    def get_object(self):
        """Возвращаем текущего пользователя."""
        return self.request.user

    def get(self, request, *args, **kwargs):
        """Возврат профиля в формате JSON."""
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        """Полное обновление профиля."""
        serializer = self.get_serializer(self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
