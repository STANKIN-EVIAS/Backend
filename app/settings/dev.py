import dj_database_url

from .aws_storage import *  # noqa: F403
from .base import *  # noqa: F403

DEBUG = True
ALLOWED_HOSTS = ["*"]


DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASES = {"default": dj_database_url.config(default=DATABASE_URL)}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}
