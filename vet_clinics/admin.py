from django.contrib import admin

from .models import Appointment, Clinic, ClinicService, Service, Veterinarian


# 🔗 Inline для связи Clinic ↔ Service
class ClinicServiceInline(admin.TabularInline):
    model = ClinicService
    extra = 1
    autocomplete_fields = ("service",)
    fields = ("service", "price_override", "available")
    verbose_name = "Услуга клиники"
    verbose_name_plural = "Услуги клиники"


# 🏥 Клиника
@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "phone_number", "email")
    search_fields = ("name", "address", "phone_number", "email")
    ordering = ("name",)
    inlines = [ClinicServiceInline]


# 🩺 Ветеринар
@admin.register(Veterinarian)
class VeterinarianAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "clinic", "specialization")
    list_filter = ("clinic", "specialization")
    search_fields = ("user__username", "user__first_name", "user__last_name", "specialization")
    ordering = ("user__last_name",)
    autocomplete_fields = ("clinic", "user")

    fieldsets = (
        ("Основная информация", {"fields": ("user", "clinic", "specialization")}),
        ("Описание", {"fields": ("bio",)}),
    )


# 💉 Услуга
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "duration_minutes")
    search_fields = ("name",)
    ordering = ("name",)
    # inline с клиниками не нужен, связи можно смотреть через Clinic

    fieldsets = (
        ("Общая информация", {"fields": ("name", "description")}),
        ("Параметры услуги", {"fields": ("price", "duration_minutes")}),
    )


# 📅 Приём
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "pet", "clinic", "veterinarian", "service", "appointment_date", "created_at")
    list_filter = ("clinic", "veterinarian", "service", "appointment_date")
    search_fields = ("pet__name", "veterinarian__user__first_name", "veterinarian__user__last_name", "service__name")
    ordering = ("-appointment_date",)
    autocomplete_fields = ("pet", "clinic", "veterinarian", "service")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Основная информация", {"fields": ("pet", "clinic", "veterinarian", "service")}),
        ("Детали приёма", {"fields": ("appointment_date", "notes")}),
        ("Служебное", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )
