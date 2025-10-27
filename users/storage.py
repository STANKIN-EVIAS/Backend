
from app.settings.aws_storage import AWS_S3_DOMAIN_URL, AWS_S3_ENDPOINT_URL, AWS_STORAGE_BUCKET_NAME, ImageStorage


class UserImageStorage(ImageStorage):
    @staticmethod
    def image_path(instance, filename):
        """
        Генерирует путь для загрузки изображений пользователей.
        """
        username = instance.username.replace(" ", "_").lower() if instance.username else "unknown_user"
        return f"users_images/{username}/{filename}"
