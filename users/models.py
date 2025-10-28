from django.contrib.auth.models import AbstractUser
from django.db import models

from users.storage import UserImageStorage


class User(AbstractUser):
    """
    Расширенная модель пользователя системы.

    Поддерживает три роли:
    - user: обычный пользователь (владелец питомцев)
    - vet: ветеринар
    - admin: администратор системы

    Для аутентификации используется email вместо username.
    """

    class Meta:
        db_table = '"users"."user"'
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    username = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        unique=True,
        verbose_name="Имя пользователя",
        help_text="Необязательное поле. Может использоваться для отображения.",
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
        help_text="Email пользователя. Используется для входа в систему.",
    )
    image = models.ImageField(
        upload_to=UserImageStorage.image_path,
        storage=UserImageStorage(),
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Фотография или аватар пользователя.",
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True,
        verbose_name="Номер телефона",
        help_text="Контактный номер телефона пользователя.",
    )
    role = models.CharField(
        max_length=50,
        default="user",
        verbose_name="Роль",
        help_text="Роль пользователя в системе (user, vet, admin).",
    )
    pets = models.ManyToManyField(
        "pets.Pet",
        through="pets.UserPet",
        related_name="owners",
        verbose_name="Питомцы",
        help_text="Питомцы, связанные с пользователем.",
    )

    # Используем email как поле для входа
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
