from django.contrib import admin
from .models import Clinic, Veterinarian, Service, Appointment


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "phone_number", "email")
    search_fields = ("name", "address", "phone_number", "email")
    ordering = ("name",)

    fieldsets = (
        ("Основная информация", {
            "fields": ("name", "address", "phone_number", "email", "website")
        }),
        ("Описание", {
            "fields": ("description",)
        })
    )


@admin.register(Veterinarian)
class VeterinarianAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "clinic", "specialization")
    list_filter = ("clinic", "specialization")
    search_fields = ("user__username", "user__first_name", "user__last_name", "specialization")
    ordering = ("user__last_name",)
    autocomplete_fields = ("clinic", "user")

    fieldsets = (
        ("Основная информация", {
            "fields": ("user", "clinic", "specialization")
        }),
        ("Описание", {
            "fields": ("bio",)
        }),
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "clinic", "price", "duration_minutes")
    list_filter = ("clinic",)
    search_fields = ("name", "clinic__name")
    ordering = ("clinic", "name")
    autocomplete_fields = ("clinic",)

    fieldsets = (
        ("Общая информация", {
            "fields": ("clinic", "name", "description")
        }),
        ("Параметры услуги", {
            "fields": ("price", "duration_minutes")
        }),
    )


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "pet",
        "clinic",
        "veterinarian",
        "service",
        "appointment_date",
        "created_at"
    )
    list_filter = ("clinic", "veterinarian", "service", "appointment_date")
    search_fields = (
        "pet__name",
        "veterinarian__user__first_name",
        "veterinarian__user__last_name",
        "service__name"
    )
    ordering = ("-appointment_date",)
    autocomplete_fields = ("pet", "clinic", "veterinarian", "service")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Основная информация", {
            "fields": ("pet", "clinic", "veterinarian", "service")
        }),
        ("Детали приёма", {
            "fields": ("appointment_date", "notes")
        }),
        ("Служебное", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )
