from django.apps import AppConfig


class PetsConfig(AppConfig):
    """Конфигурация приложения pets."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pets'
    verbose_name = "Питомцы"