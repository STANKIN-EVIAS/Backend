from django.contrib import admin
from .models import AnimalCategory, Species, Pet, UserPet

@admin.register(AnimalCategory)
class AnimalCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # колонки для отображения
    search_fields = ('name',)      # поиск по имени
    ordering = ('name',)           # сортировка по имени

@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')  # показываем категорию
    list_filter = ('category',)               # фильтр по категории
    search_fields = ('name',)                 # поиск по имени
    ordering = ('category', 'name')

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'species', 'birth_date', 'gender')  # основные поля
    list_filter = ('species', 'gender')                               # фильтры
    search_fields = ('name', 'description')                           # поиск
    ordering = ('name',)
    readonly_fields = ('id',)

@admin.register(UserPet)
class UserPetAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pet')  # показываем пользователя, питомца и дату добавления
    list_filter = ('user',)               # фильтры
    search_fields = ('user__username', 'pet__name')  # поиск по имени пользователя и питомца
