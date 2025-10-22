from django.db import models
from django.contrib.auth.models import AbstractUser

from users.storage import UserImageStorage


class User(AbstractUser):
    class Meta:
        db_table = '"users"."user"'
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    username = models.CharField(max_length=150, blank=True, null=True, unique=True)
    email = models.EmailField(unique=True, verbose_name="Email")
    image = models.ImageField(
        upload_to=UserImageStorage.image_path,
        storage=UserImageStorage(),
        blank=True,
        null=True,
        verbose_name="Аватар",
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True, unique=True, verbose_name="Номер телефона")
    role = models.CharField(max_length=50, default="user", verbose_name="Роль")  # user, vet, admin
    pets = models.ManyToManyField("pets.Pet", through="pets.UserPet", related_name="owners")

    # Используем email как поле для входа
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
