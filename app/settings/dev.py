from .base import *  # noqa: F403
from .logging import LOGGING  # noqa: F401
from .aws_storage import *  # noqa: F403
import dj_database_url

DEBUG = True
ALLOWED_HOSTS = ["*"]


DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASES = {"default": dj_database_url.config(default=DATABASE_URL)}
