from django.db import models

from pets.models import Pet
from pets_documents.storage import PetFileImageStorage


# 🪪 ПАСПОРТ ПИТОМЦА
class Passport(models.Model):
    class Meta:
        db_table = '"pets_documents"."passport"'
        verbose_name = "Паспорт питомца"
        verbose_name_plural = "Паспорта питомцев"
        ordering = ["-issue_date"]

    passport_number = models.CharField(max_length=50, unique=True, verbose_name="Номер паспорта")
    pet = models.OneToOneField(Pet, on_delete=models.CASCADE, related_name="passport", verbose_name="Питомец")
    issue_date = models.DateField(auto_now_add=True, verbose_name="Дата выдачи")
    issued_by = models.CharField(null=True, blank=True, max_length=255, verbose_name="Кем выдан")
    microchip_number = models.CharField(max_length=100, null=True, blank=True, verbose_name="Номер микрочипа")
    country_of_issue = models.CharField(max_length=100, null=True, blank=True, verbose_name="Страна выдачи")
    photo = models.ImageField(upload_to="pets/passports/", null=True, blank=True, verbose_name="Фото паспорта")

    def __str__(self):
        return f"{self.pet.name} — {self.passport_number}"


# 📜 СЕРТИФИКАТ (вакцинация, родословная, стерилизация и т.п.)
class Certificate(models.Model):
    class Meta:
        db_table = '"pets_documents"."certificate"'
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"
        ordering = ["-issue_date"]

    certificate_number = models.CharField(
        max_length=50, null=True, blank=True, unique=True, verbose_name="Номер сертификата"
    )
    CERTIFICATE_TYPES = [
        ("vaccination", "Вакцинация"),
        ("sterilization", "Стерилизация"),
        ("pedigree", "Родословная"),
        ("training", "Тренировка / курс"),
        ("other", "Прочее"),
    ]

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="certificates", verbose_name="Питомец")
    certificate_type = models.CharField(max_length=50, choices=CERTIFICATE_TYPES, verbose_name="Тип сертификата")
    title = models.CharField(null=True, blank=True, max_length=255, verbose_name="Название документа")
    issue_date = models.DateField(null=True, blank=True, auto_now_add=True, verbose_name="Дата выдачи")
    expiration_date = models.DateField(null=True, blank=True, verbose_name="Срок действия")
    issued_by = models.CharField(null=True, blank=True, max_length=255, verbose_name="Кем выдан")
    description = models.TextField(null=True, blank=True, verbose_name="Описание / комментарий")
    document_file = models.FileField(
        upload_to=PetFileImageStorage.image_path,
        storage=PetFileImageStorage(),
        blank=True,
        null=True,
        verbose_name="Файл сертификата",
    )

    def __str__(self):
        return f"{self.get_certificate_type_display()} — {self.pet.name}"


# 🩺 МЕДИЦИНСКАЯ КАРТА
class MedicalCard(models.Model):
    class Meta:
        db_table = '"pets_documents"."medical_card"'
        verbose_name = "Медицинская карта"
        verbose_name_plural = "Медицинские карты"

    medical_number = models.CharField(max_length=50, null=True, blank=True, unique=True, verbose_name="Номер медкарты")
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="medical_cards", verbose_name="Питомец")
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Вес (кг)")
    blood_type = models.CharField(max_length=10, null=True, blank=True, verbose_name="Группа крови")
    allergies = models.TextField(null=True, blank=True, verbose_name="Аллергии")
    chronic_diseases = models.TextField(null=True, blank=True, verbose_name="Хронические заболевания")
    vaccinations = models.TextField(null=True, blank=True, verbose_name="Прививки (описание)")
    last_checkup_date = models.DateField(null=True, blank=True, verbose_name="Последний осмотр")
    next_checkup_date = models.DateField(null=True, blank=True, verbose_name="Следующий осмотр")
    certificate = models.ForeignKey(
        Certificate,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="medical_cards",
        verbose_name="Связанный сертификат",
    )

    def __str__(self):
        return f"Медкарта — {self.pet.name}"
