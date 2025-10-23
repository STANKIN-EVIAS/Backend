from rest_framework import serializers
from .models import Clinic, Pet


class ClinicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clinic
        fields = ["id", "name", "address", "phone_number", "email", "website", "description"]


from rest_framework import serializers
from .models import Veterinarian


class VeterinarianSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    email = serializers.CharField(source="user.email", read_only=True)
    clinic_name = serializers.CharField(source="clinic.name", read_only=True)

    class Meta:
        model = Veterinarian
        fields = ["id", "full_name", "email", "specialization", "bio", "clinic_name"]

    def get_full_name(self, obj):
        return obj.user.get_full_name()
