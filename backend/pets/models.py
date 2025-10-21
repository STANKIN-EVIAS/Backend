from django.db import models
from pets.storage import PetImageStorage
from users.models import User

# Категории животных
class AnimalGenus(models.Model):
    class Meta:
        db_table = '"pets"."animal_genus"'
        verbose_name = "Род животных"
        verbose_name_plural = "Категории животных"
    
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Породы
class Species(models.Model):
    class Meta:
        db_table = '"pets"."species"'
        verbose_name = "Порода"
        verbose_name_plural = "Породы"
    
    category = models.ForeignKey(AnimalGenus , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Питомцы
class Pet(models.Model):
    class Meta:
        db_table = '"pets"."pets"'
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"
    
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to=PetImageStorage.image_path,
        storage=PetImageStorage(),
        blank=True,
        null=True,
        verbose_name="Аватар",
    )
    birth_date = models.DateField(null=True, blank=True)

    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский')
    ]

    gender = models.CharField(
        max_length=1,       # достаточно 1 символа для кода
        choices=GENDER_CHOICES,
        blank=True,
        null=True          
    )

    genus  = models.ForeignKey(AnimalGenus , null=True, blank=True, on_delete=models.SET_NULL)
    species = models.ForeignKey(Species, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

# Промежуточная таблица для связи User ↔ Pet
class UserPet(models.Model):
    class Meta:
        db_table = '"pets"."users_pets"'
        verbose_name = "Питомец пользователя"
        verbose_name_plural = "Питомцы пользователей"
        unique_together = ('user', 'pet')  # запрещаем дубли одной пары
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} ↔ {self.pet.name}"