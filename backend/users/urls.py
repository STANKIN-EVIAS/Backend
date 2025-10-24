from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserProfileAPIView

router = DefaultRouter()
router.register(r"", UserViewSet, basename="user")

urlpatterns = [
    path("profile/", UserProfileAPIView.as_view(), name="profile"),
    path("", include(router.urls)),
]
