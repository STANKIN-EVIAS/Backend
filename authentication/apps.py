from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """Конфигурация приложения auth."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "authentication"
    verbose_name = "Аутентификация"
