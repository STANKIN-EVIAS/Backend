"""
Маршрутизация проекта EVIAS.
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
                path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
                path("", include("users.urls")),  # login, register, profile
            ]
        ),
    ),
    path("users/", include("users.urls")),
    path("pets/", include("pets.urls")),
    path("clinics/", include("vet_clinics.urls")),
]

urlpatterns = [
    # Административная панель
    path("admin/", admin.site.urls),
    # API v1
    path("", include(api_v1_patterns)),
    # API документация
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

# Настройка раздачи медиа-файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
