from rest_framework import serializers
from .models import User
from pets.models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'name', 'image', 'birth_date', 'gender', 'description', 'species']

