
from app.settings.aws_storage import AWS_S3_DOMAIN_URL, AWS_S3_ENDPOINT_URL, AWS_STORAGE_BUCKET_NAME, ImageStorage


class PetFileImageStorage(ImageStorage):
    @staticmethod
    def image_path(instance, filename):
        """
        Генерирует путь для загрузки изображений пользователей.
        """
        pet_name = instance.pet.name.replace(" ", "_").lower()
        pet_id = instance.pet.id
        pet_id_name = f"{pet_id}_{pet_name}"

        return f"pets_images/{pet_id_name}/{filename}"
