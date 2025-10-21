from django.urls import path, include
from rest_framework.routers import DefaultRouter

from pets.views import PetsViewSet
from .views import UserViewSet, RegisterView, LoginView, UserProfileAPIView

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path("profile/", UserProfileAPIView.as_view(), name="profile"),
    path('', include(router.urls)), 
]
