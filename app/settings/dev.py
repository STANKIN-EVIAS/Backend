from .base import *
from .logging import LOGGING
from .aws_storage import *
import dj_database_url

DEBUG = True
ALLOWED_HOSTS = ["*"]


DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASES = {"default": dj_database_url.config(default=DATABASE_URL)}
