from .base import *
from .logging import LOGGING
import dj_database_url

DEBUG = True
ALLOWED_HOSTS = ['*']

# Database
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "evias",
#         "USER": "evias",
#         "PASSWORD": "kosyakino",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }

DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASES = {
    "default": dj_database_url.config(default=DATABASE_URL)
}