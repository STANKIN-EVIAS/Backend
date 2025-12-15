from rest_framework import serializers

from .models import Appointment, Clinic, Service, Treatment, Veterinarian


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "name", "description", "price", "duration_minutes"]


class ClinicSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)

    class Meta:
        model = Clinic
        fields = "__all__"


class VeterinarianSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    email = serializers.CharField(source="user.email", read_only=True)
    clinic_name = serializers.CharField(source="clinic.name", read_only=True)

    class Meta:
        model = Veterinarian
        fields = ["id", "full_name", "email", "specialization", "bio", "clinic_name"]

    def get_full_name(self, obj) -> str:
        return obj.user.get_full_name()


class AppointmentSerializer(serializers.ModelSerializer):
    # Эти поля добавят имена питомца и клиники в JSON
    clinic_name = serializers.CharField(source="clinic.name", read_only=True)
    pet_name = serializers.CharField(source="pet.name", read_only=True)
    service_name = serializers.CharField(source="service.name", read_only=True)
    user_name = serializers.CharField(source="user.get_full_name", read_only=True)

    class Meta:
        model = Appointment
        # Здесь можно указать явно все поля + clinic_name и pet_name
        fields = [
            "id",
            "user",
            "user_name",
            "pet",
            "pet_name",
            "clinic",
            "clinic_name",
            "veterinarian",
            "service",
            "service_name",
            "appointment_date",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["user", "created_at", "updated_at"]


class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = "__all__"
        read_only_fields = ["veterinarian", "created_at"]
