from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from pets.models import UserPet, Pet

# Inline для отображения питомцев пользователя
class UserPetInline(admin.TabularInline):
    model = UserPet
    extra = 0  # не показывать пустые строки по умолчанию
    autocomplete_fields = ('pet',)   # автозаполнение питомцев

# Кастомный админ для пользователя
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = [UserPetInline]  # подключаем инлайн
    list_display = ('username', 'email', 'phone_number', 'role')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'phone_number')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Личная информация', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'image')}),
        ('Права доступа', {'fields': ('role', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
