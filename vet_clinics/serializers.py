from rest_framework import serializers

from .models import Clinic, Service, Veterinarian


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

    def get_full_name(self, obj):
        return obj.user.get_full_name()
