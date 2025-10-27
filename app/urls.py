"""
Маршрутизация проекта EVIAS.
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

# Swagger/OpenAPI документация
schema_view = get_schema_view(
    openapi.Info(
        title="EVIAS API",
        default_version="v1",
        description="API системы для ветеринарных клиник",
        contact=openapi.Contact(email="admin@evias.ru"),
        license=openapi.License(name="Private License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# API v1 URLs
api_v1_patterns = [
    path(
        "auth/",
        include(
            [
                path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
                path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
                path("", include("authentication.urls")),  # login, register
            ]
        ),
    ),
    path("users/", include("users.urls")),
    path("pets/", include("pets.urls")),
    path("vet-clinics/", include("vet_clinics.urls")),
]
urlpatterns = [
    # Административная панель
    path("admin/", admin.site.urls),
    # API v1
    path("", include(api_v1_patterns)),
    # Метрики Prometheus
    path("", include("django_prometheus.urls")),
    # Схема OpenAPI (JSON)
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Swagger UI (c JWT кнопкой)
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    # ReDoc (альтернативный интерфейс)
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

# Настройка раздачи медиа-файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
