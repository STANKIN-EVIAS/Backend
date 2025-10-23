"""Маршрутизация проекта EVIAS.

Главные URL-ы приложения подключают `users` и стандартные JWT-эндпоинты.
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("pets/", include("pets.urls")),
    path("vet-clinics/", include("vet_clinics.urls")),
]


urlpatterns += [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
