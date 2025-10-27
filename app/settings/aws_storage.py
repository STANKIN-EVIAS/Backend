# storage

import os
from pathlib import Path
from storages.backends.s3boto3 import S3Boto3Storage

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_S3_ENDPOINT_URL = "https://storage.yandexcloud.net"
AWS_STORAGE_BUCKET_NAME = "evias-media"
AWS_S3_DOMAIN_URL = "storage.yandexcloud.net"
AWS_S3_REGION_NAME = "ru-central1"
AWS_QUERYSTRING_AUTH = False  # отключает подписи в URL, для прямого доступа
AWS_DEFAULT_ACL = None

MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/"
MEDIA_ROOT = BASE_DIR / "media"

class ImageStorage(S3Boto3Storage):
    bucket_name = AWS_STORAGE_BUCKET_NAME
    endpoint_url = AWS_S3_ENDPOINT_URL
    file_overwrite = False
    custom_domain = f"{AWS_S3_DOMAIN_URL}/{bucket_name}"

    @staticmethod
    def image_path(filename):
        return f"other/{filename}"