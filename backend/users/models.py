from django.db import models
from django.contrib.auth.models import AbstractUser



# Пользователь
class User(AbstractUser):
    image = models.ImageField(
        # upload_to=UserImageStorage.image_path,
        # storage=UserImageStorage(),
        blank=True,
        null=True,
        verbose_name="Аватар",
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True, unique=True, verbose_name="Номер телефона")
    email = models.EmailField(unique=True, verbose_name="Email")
    role = models.CharField(max_length=50, default='user')  # user, vet, admin

    # Many-to-Many связь с питомцами через промежуточную таблицу
    pets = models.ManyToManyField(
        'pets.Pet',
        through='pets.UserPet',
        related_name='owners'
    )

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"