from django.contrib import admin
from .models import Passport, Certificate, MedicalCard
from pets.models import Pet


# ===============================
# Inline блоки для Pet
# ===============================
class PassportInline(admin.StackedInline):
    model = Passport
    extra = 0
    can_delete = True
    readonly_fields = ("issue_date",)
    fieldsets = (
        ("Паспорт питомца", {
            "fields": (
                "passport_number",
                "issue_date",
                "issued_by",
                "country_of_issue",
                "microchip_number",
                "photo",
            )
        }),
    )


class CertificateInline(admin.TabularInline):
    model = Certificate
    extra = 0
    can_delete = True
    fields = (
        "certificate_number",
        "certificate_type",
        "title",
        "issue_date",
        "expiration_date",
        "issued_by",
        "document_file",
    )
    readonly_fields = ("issue_date",)
    show_change_link = True


class MedicalCardInline(admin.StackedInline):
    model = MedicalCard
    extra = 0
    can_delete = True
    fieldsets = (
        ("Медицинская информация", {
            "fields": (
                "medical_number",
                "weight",
                "blood_type",
                "allergies",
                "chronic_diseases",
                "vaccinations",
                "last_checkup_date",
                "next_checkup_date",
                "certificate",
            )
        }),
    )
    show_change_link = True


# ===============================
# Регистрация самих моделей
# ===============================
@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = (
        "passport_number", "pet", "issue_date", "issued_by", "country_of_issue", "microchip_number"
    )
    list_filter = ("country_of_issue", "issue_date")
    search_fields = ("passport_number", "pet__name", "microchip_number", "issued_by")
    readonly_fields = ("issue_date",)
    ordering = ("-issue_date",)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        "certificate_number", "pet", "certificate_type", "title",
        "issue_date", "expiration_date", "issued_by",
    )
    list_filter = ("certificate_type", "issue_date", "expiration_date")
    search_fields = ("certificate_number", "pet__name", "issued_by", "title")
    readonly_fields = ("issue_date",)
    ordering = ("-issue_date",)


@admin.register(MedicalCard)
class MedicalCardAdmin(admin.ModelAdmin):
    list_display = (
        "medical_number", "pet", "weight", "blood_type",
        "last_checkup_date", "next_checkup_date", "certificate",
    )
    list_filter = ("blood_type", "last_checkup_date", "next_checkup_date")
    search_fields = ("medical_number", "pet__name", "blood_type")
    ordering = ("-last_checkup_date",)



