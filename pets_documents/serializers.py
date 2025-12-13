from rest_framework import serializers

from .models import Certificate, MedicalCard, Passport


class CertificateSerializer(serializers.ModelSerializer):
    certificate_type_display = serializers.CharField(source="get_certificate_type_display", read_only=True)
    pet_name = serializers.CharField(source="pet.name", read_only=True)

    class Meta:
        model = Certificate
        fields = [
            "id",
            "certificate_number",
            "certificate_type",
            "certificate_type_display",
            "pet",
            "pet_name",
            "title",
            "issue_date",
            "expiration_date",
            "issued_by",
            "description",
            "document_file",
        ]
        read_only_fields = ["id", "issue_date"]


class MedicalCardSerializer(serializers.ModelSerializer):
    certificate_info = CertificateSerializer(source="certificate", read_only=True)
    pet_name = serializers.CharField(source="pet.name", read_only=True)

    class Meta:
        model = MedicalCard
        fields = [
            "id",
            "medical_number",
            "pet",
            "pet_name",
            "weight",
            "blood_type",
            "allergies",
            "chronic_diseases",
            "vaccinations",
            "last_checkup_date",
            "next_checkup_date",
            "certificate",
            "certificate_info",
        ]
        read_only_fields = ["id"]


class PassportSerializer(serializers.ModelSerializer):
    pet_name = serializers.CharField(source="pet.name", read_only=True)
    pet_species = serializers.CharField(source="pet.species", read_only=True)
    pet_breed = serializers.CharField(source="pet.breed", read_only=True)

    class Meta:
        model = Passport
        fields = [
            "id",
            "passport_number",
            "pet",
            "pet_name",
            "pet_species",
            "pet_breed",
            "issue_date",
            "issued_by",
            "microchip_number",
            "country_of_issue",
            "photo",
        ]
        read_only_fields = ["id", "issue_date"]


# Сериализатор для детального отображения питомца со всеми документами
class PetDocumentsSerializer(serializers.Serializer):
    passport = PassportSerializer(read_only=True)
    certificates = CertificateSerializer(many=True, read_only=True)
    medical_cards = MedicalCardSerializer(many=True, read_only=True)
