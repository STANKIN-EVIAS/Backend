from django.contrib import admin
from .models import Passport, Certificate, MedicalCard


# ===============================
# 🪪 ПАСПОРТ
# ===============================
@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = (
        "passport_number",
        "pet",
        "issue_date",
        "issued_by",
        "country_of_issue",
        "microchip_number",
    )
    list_filter = ("country_of_issue", "issue_date")
    search_fields = ("passport_number", "pet__name", "microchip_number", "issued_by")
    readonly_fields = ("issue_date",)
    ordering = ("-issue_date",)
    fieldsets = (
        ("Основная информация", {
            "fields": (
                "passport_number",
                "pet",
                "issue_date",
                "issued_by",
                "country_of_issue",
            )
        }),
        ("Дополнительно", {
            "fields": ("microchip_number", "photo"),
            "classes": ("collapse",)
        }),
    )


# ===============================
# 📜 СЕРТИФИКАТ
# ===============================
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        "certificate_number",
        "pet",
        "certificate_type",
        "title",
        "issue_date",
        "expiration_date",
        "issued_by",
    )
    list_filter = ("certificate_type", "issue_date", "expiration_date")
    search_fields = ("certificate_number", "pet__name", "issued_by", "title")
    readonly_fields = ("issue_date",)
    ordering = ("-issue_date",)

    fieldsets = (
        ("Основная информация", {
            "fields": (
                "certificate_number",
                "pet",
                "certificate_type",
                "title",
                "issued_by",
                "issue_date",
                "expiration_date",
            )
        }),
        ("Дополнительно", {
            "fields": ("description", "document_file"),
            "classes": ("collapse",)
        }),
    )

    # красивое отображение файла (если загружен)
    def document_link(self, obj):
        if obj.document_file:
            return f"<a href='{obj.document_file.url}' target='_blank'>Открыть файл</a>"
        return "—"
    document_link.allow_tags = True
    document_link.short_description = "Файл"


# ===============================
# 🩺 МЕДИЦИНСКАЯ КАРТА
# ===============================
@admin.register(MedicalCard)
class MedicalCardAdmin(admin.ModelAdmin):
    list_display = (
        "medical_number",
        "pet",
        "weight",
        "blood_type",
        "last_checkup_date",
        "next_checkup_date",
        "certificate",
    )
    list_filter = ("blood_type", "last_checkup_date", "next_checkup_date")
    search_fields = ("medical_number", "pet__name", "blood_type")
    ordering = ("-last_checkup_date",)
    fieldsets = (
        ("Основная информация", {
            "fields": (
                "medical_number",
                "pet",
                "weight",
                "blood_type",
                "certificate",
            )
        }),
        ("Медицинские данные", {
            "fields": (
                "allergies",
                "chronic_diseases",
                "vaccinations",
                "last_checkup_date",
                "next_checkup_date",
            ),
        }),
    )
