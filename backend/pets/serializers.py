from rest_framework import serializers
from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    genus = serializers.CharField(source="genus.name", read_only=True)
    species = serializers.CharField(source="species.name", read_only=True)
    gender = serializers.CharField(source="get_gender_display", read_only=True)

    class Meta:
        model = Pet
        fields = ["id", "name", "image", "birth_date", "gender", "genus", "species"]
