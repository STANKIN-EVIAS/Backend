from django.contrib import admin
from django.utils.html import format_html
from .models import AnimalGenus, Species, Pet, UserPet
from users.models import User

# --- Категории животных ---
@admin.register(AnimalGenus)
class AnimalGenusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)

# --- Породы ---
@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('category', 'name')

# --- Питомцы ---
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'species', 'genus', 'birth_date', 'gender')
    list_filter = ('species', 'gender', 'genus')
    search_fields = ('name', 'description', 'species__name')
    ordering = ('name',)
    readonly_fields = ('id',)




# --- Питомцы пользователей ---
@admin.register(UserPet)
class UserPetAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pet', 'pet_species', 'pet_genus')
    list_filter = ('user', 'pet__species__category')
    search_fields = ('user__username', 'pet__name')
    readonly_fields = ('id',)

    def pet_species(self, obj):
        return obj.pet.species.name if obj.pet and obj.pet.species else None
    pet_species.short_description = "Порода"

    def pet_genus(self, obj):
        return obj.pet.genus.name if obj.pet and obj.pet.genus else None


# --- Инлайн для пользователей (если нужно) ---
class UserPetInline(admin.TabularInline):
    model = UserPet
    extra = 0
    readonly_fields = ('pet',)
    can_delete = False

