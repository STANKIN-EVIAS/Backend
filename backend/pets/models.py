from django.db import models
from users.models import User

# Категории животных
class AnimalCategory(models.Model):
    class Meta:
        db_table = "animal_categories"
        verbose_name = "Категория животных"
        verbose_name_plural = "Категории животных"
    
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Породы
class Species(models.Model):
    class Meta:
        db_table = "species"
        verbose_name = "Порода"
        verbose_name_plural = "Породы"
    
    category = models.ForeignKey(AnimalCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Питомцы
class Pet(models.Model):
    class Meta:
        db_table = "pets"
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"
    
    name = models.CharField(max_length=100)
    image = models.ImageField(
        # upload_to=UserImageStorage.image_path,
        # storage=UserImageStorage(),
        blank=True,
        null=True,
        verbose_name="Аватар",
    )
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    description = models.TextField(blank=True)
    species = models.ForeignKey(Species, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

# Промежуточная таблица для связи User ↔ Pet
class UserPet(models.Model):
    class Meta:
        db_table = "users_pets"
        verbose_name = "Питомец пользователя"
        verbose_name_plural = "Питомцы пользователей"
        unique_together = ('user', 'pet')  # запрещаем дубли одной пары
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ↔ {self.pet.name}"