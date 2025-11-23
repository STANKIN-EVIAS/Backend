from rest_framework import serializers

from .models import AnimalGenus, Pet, Species, UserPet


class AnimalGenusSerializer(serializers.ModelSerializer):
    """
    Сериализатор для родов животных (кошки, собаки и т.д.).

    Используется для:
    - Получения списка доступных родов животных
    - Базовой информации о роде в других сериализаторах

    Поля:
    - id: уникальный идентификатор
    - name: название рода животных
    """

    class Meta:
        model = AnimalGenus
        fields = ["id", "name"]


class SpeciesSerializer(serializers.ModelSerializer):
    """
    Сериализатор для пород животных.

    Используется для:
    - Получения списка пород
    - Создания/обновления информации о породах
    - Отображения информации о породе в других сериализаторах

    Поля:
    - id: уникальный идентификатор
    - name: название породы
    - genus: ID рода животных (AnimalGenus)
    - genus_name: название рода животных (только для чтения)
    """

    genus_name = serializers.CharField(
        source="genus.name", read_only=True, help_text="Название рода животных, к которому относится порода"
    )

    class Meta:
        model = Species
        fields = ["id", "name", "genus", "genus_name"]


class PetSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания и отображения питомцев.

    Используется для:
    - создания питомца с genus_id и species_id
    - отображения genus_name и species_name при чтении
    """

    # поля только для чтения (отображаются красиво)
    genus = serializers.CharField(source="genus.name", read_only=True, help_text="Название рода животных")
    species = serializers.CharField(source="species.name", read_only=True, help_text="Название породы животных")
    age = serializers.IntegerField(read_only=True, help_text="Возраст питомца в годах")

    genus_id = serializers.PrimaryKeyRelatedField(
        queryset=AnimalGenus.objects.all(),
        source="genus",
        required=False,
        allow_null=True,
        help_text="ID рода животного",
    )
    species_id = serializers.PrimaryKeyRelatedField(
        queryset=Species.objects.all(),
        source="species",
        required=False,
        allow_null=True,
        help_text="ID породы животного",
    )

    class Meta:
        model = Pet
        fields = ["id", "name", "image", "birth_date", "age", "gender", "genus_id", "species_id", "genus", "species"]
        extra_kwargs = {
            "image": {"required": False, "allow_null": True},
            "birth_date": {"required": False, "allow_null": True},
            "gender": {"required": False, "allow_null": True},
        }

    def get_age(self, obj):
        """Рассчитывает возраст питомца в годах и месяцах."""
        if not obj.birth_date:
            return None

        from datetime import date

        today = date.today()
        birth = obj.birth_date

        # базовые расчёты
        years = today.year - birth.year
        months = today.month - birth.month

        # если месяц еще не наступил — уменьшаем год и добавляем месяцев
        if today.day < birth.day:
            months -= 1

        if months < 0:
            years -= 1
            months += 12

        # формат ответа
        return {"years": years, "months": months}

    def to_representation(self, instance):
        """
        Переопределяем to_representation, чтобы добавить вычисляемое поле age.
        """
        data = super().to_representation(instance)
        if self.get_age(instance):
            data["age"] = self.get_age(instance)
        return data

    def get_owners_count(self, obj):
        """Возвращает количество владельцев питомца."""
        return obj.owners.count()


class PetDetailSerializer(PetSerializer):
    """
    Расширенный сериализатор для детальной информации о питомце.

    Наследуется от PetSerializer и добавляет информацию о владельцах.
    Используется при детальном просмотре информации о конкретном питомце.

    Дополнительные поля:
    - owners: список владельцев питомца (краткая информация о каждом)

    Пример использования:
    GET /pets/{id}/ -> вернет детальную информацию с владельцами
    """

    owners = serializers.SerializerMethodField(help_text="Список владельцев питомца")

    class Meta(PetSerializer.Meta):
        fields = PetSerializer.Meta.fields + ["owners"]

    def get_owners(self, obj) -> list[str]:
        """Возвращает список владельцев с краткой информацией о каждом."""
        from users.serializers import UserBriefSerializer

        return UserBriefSerializer(obj.owners.all(), many=True).data


class UserPetSerializer(serializers.ModelSerializer):
    """
    Сериализатор для управления связями пользователь-питомец.

    Используется для:
    - Получения списка питомцев пользователя
    - Добавления существующего питомца пользователю
    - Управления правами владения

    Поля:
    - id: уникальный идентификатор связи
    - pet: полная информация о питомце (только для чтения)
    - pet_id: ID питомца для создания связи (только для записи)

    Пример использования:
    POST /api/v1/pets/my/ с {'pet_id': 123} -> добавит питомца пользователю
    """

    pet = PetSerializer(read_only=True, help_text="Полная информация о питомце")
    pet_id = serializers.PrimaryKeyRelatedField(
        queryset=Pet.objects.all(), source="pet", write_only=True, help_text="ID питомца для создания связи"
    )

    class Meta:
        model = UserPet
        fields = ["id", "pet", "pet_id"]
