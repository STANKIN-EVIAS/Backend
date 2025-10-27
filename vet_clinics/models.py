from django.db import models
from pets.models import Pet
from users.models import User


# 🏥 КЛИНИКА
class Clinic(models.Model):
    class Meta:
        db_table = '"vet_clinics"."clinic"'
        verbose_name = "Клиника"
        verbose_name_plural = "Клиники"
        ordering = ["name"]

    name = models.CharField(max_length=255, verbose_name="Название клиники")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    phone_number = models.CharField(max_length=50, null=True, blank=True, verbose_name="Телефон")
    email = models.EmailField(null=True, blank=True, verbose_name="Email")
    website = models.URLField(null=True, blank=True, verbose_name="Сайт")
    description = models.TextField(null=True, blank=True, verbose_name="Описание / информация о клинике")

    # Связь с услугами (многие-ко-многим)
    services = models.ManyToManyField(
        "Service",
        through="ClinicService",
        related_name="clinics",
        verbose_name="Предоставляемые услуги",
    )

    def __str__(self):
        return self.name


# 💉 УСЛУГА
class Service(models.Model):
    class Meta:
        db_table = '"vet_clinics"."service"'
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ["name"]

    name = models.CharField(max_length=255, verbose_name="Название услуги")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=8, decimal_places=0, verbose_name="Цена по умолчанию")
    duration_minutes = models.PositiveIntegerField(default=30, verbose_name="Длительность (мин)")

    def __str__(self):
        return self.name


# 🔗 ПРОМЕЖУТОЧНАЯ ТАБЛИЦА для связи "Клиника ↔ Услуга"
class ClinicService(models.Model):
    class Meta:
        db_table = '"vet_clinics"."clinic_service"'
        verbose_name = "Услуга клиники"
        verbose_name_plural = "Услуги клиник"
        unique_together = ("clinic", "service")

    clinic = models.ForeignKey(
        Clinic,
        on_delete=models.CASCADE,
        related_name="clinic_services",
        verbose_name="Клиника",
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="clinic_services",
        verbose_name="Услуга",
    )
    price_override = models.DecimalField(
        max_digits=8,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="Цена в этой клинике (если отличается)",
    )
    available = models.BooleanField(default=True, verbose_name="Доступна")

    def __str__(self):
        return f"{self.clinic.name} — {self.service.name}"


# 🩺 ВЕТЕРИНАР
class Veterinarian(models.Model):
    class Meta:
        db_table = '"vet_clinics"."veterinarian"'
        verbose_name = "Ветеринар"
        verbose_name_plural = "Ветеринары"
        ordering = ["user__last_name"]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="veterinarian_profile", verbose_name="Пользователь"
    )
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name="veterinarians", verbose_name="Клиника")
    specialization = models.CharField(max_length=255, verbose_name="Специализация")
    bio = models.TextField(null=True, blank=True, verbose_name="Биография / описание")

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.specialization})"


# 📅 ПРИЁМ
class Appointment(models.Model):
    class Meta:
        db_table = '"vet_clinics"."appointment"'
        verbose_name = "Приём"
        verbose_name_plural = "Приёмы"
        ordering = ["-appointment_date"]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments", verbose_name="Пользователь")
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="appointments", verbose_name="Питомец")
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name="appointments", verbose_name="Клиника")
    veterinarian = models.ForeignKey(
        Veterinarian,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="appointments",
        verbose_name="Ветеринар",
    )
    service = models.ForeignKey(
        Service, on_delete=models.SET_NULL, null=True, blank=True, related_name="appointments", verbose_name="Услуга"
    )
    appointment_date = models.DateTimeField(verbose_name="Дата и время приёма")
    notes = models.TextField(null=True, blank=True, verbose_name="Комментарий / примечание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    def __str__(self):
        return f"{self.pet.name} — {self.service.name if self.service else 'Приём'} ({self.appointment_date:%d.%m.%Y %H:%M})"


# 💊 ЛЕЧЕНИЕ
class Treatment(models.Model):
    class Meta:
        db_table = '"vet_clinics"."treatment"'
        verbose_name = "Лечебная процедура"
        verbose_name_plural = "Лечебные процедуры"
        ordering = ["-created_at"]

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="treatments", verbose_name="Питомец")
    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="treatments",
        verbose_name="Запись на приём",
    )
    veterinarian = models.ForeignKey(
        Veterinarian,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="treatments",
        verbose_name="Ветеринар",
    )
    diagnosis = models.TextField(verbose_name="Диагноз")
    procedure = models.TextField(verbose_name="Проведённая процедура")
    cost = models.DecimalField(max_digits=8, decimal_places=0, verbose_name="Стоимость")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.pet.name} — {self.diagnosis[:40]}"
