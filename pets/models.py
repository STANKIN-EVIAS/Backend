from django.db import models
from users.models import User

from pets.storage import PetImageStorage


class AnimalGenus(models.Model):
    """
    Модель для представления рода животных (кошки, собаки, и т.д.).

    Используется как верхний уровень классификации животных в системе.
    От этой модели зависят конкретные породы (Species).
    """

    class Meta:
        db_table = '"pets"."animal_genus"'
        verbose_name = "Род животных"
        verbose_name_plural = "Категории животных"

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название",
        help_text="Название рода животных (например, 'Кошки', 'Собаки')",
    )

    def __str__(self):
        return self.name


class Species(models.Model):
    """
    Модель породы животного.

    Связана с родом животных (AnimalGenus) отношением многие-к-одному.
    Каждая порода принадлежит определенному роду животных.
    """

    class Meta:
        db_table = '"pets"."species"'
        verbose_name = "Порода"
        verbose_name_plural = "Породы"

    genus = models.ForeignKey(
        AnimalGenus, on_delete=models.CASCADE, verbose_name="Род животных", help_text="К какому роду относится порода"
    )
    name = models.CharField(max_length=100, verbose_name="Название породы", help_text="Название породы животного")

    def __str__(self):
        return self.name


class Pet(models.Model):
    """
    Модель питомца.

    Основная сущность системы, представляющая конкретное животное.
    Связана с породой (Species) и родом (AnimalGenus).
    Может иметь нескольких владельцев через промежуточную модель UserPet.
    """

    class Meta:
        db_table = '"pets"."pets"'
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"

    name = models.CharField(max_length=100, verbose_name="Кличка", help_text="Кличка питомца")
    image = models.ImageField(
        upload_to=PetImageStorage.image_path,
        storage=PetImageStorage(),
        blank=True,
        null=True,
        verbose_name="Фотография",
        help_text="Фотография питомца",
    )
    birth_date = models.DateField(
        null=True, blank=True, verbose_name="Дата рождения", help_text="Дата рождения питомца"
    )

    GENDER_CHOICES = [("M", "Мужской"), ("F", "Женский")]

    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, blank=True, null=True, verbose_name="Пол", help_text="Пол питомца"
    )

    genus = models.ForeignKey(
        AnimalGenus,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Род животного",
        help_text="К какому роду относится питомец",
    )
    species = models.ForeignKey(
        Species, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Порода", help_text="Порода питомца"
    )

    def __str__(self):
        return self.name


class UserPet(models.Model):
    """
    Промежуточная модель для связи многие-ко-многим между User и Pet.

    Позволяет:
    - Связывать питомцев с несколькими владельцами
    - Одному пользователю иметь несколько питомцев
    - Отслеживать отношения владения

    Ограничение unique_together не позволяет создавать дубликаты связей.
    """

    class Meta:
        db_table = '"pets"."users_pets"'
        verbose_name = "Питомец пользователя"
        verbose_name_plural = "Питомцы пользователей"
        unique_together = ("user", "pet")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", help_text="Владелец питомца")
    pet = models.ForeignKey(
        Pet, on_delete=models.CASCADE, verbose_name="Питомец", help_text="Питомец, принадлежащий пользователю"
    )

    def __str__(self):
        return f"{self.user.username} ↔ {self.pet.name}"
