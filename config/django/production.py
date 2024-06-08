from .base import *
from config.env import env
import dj_database_url


SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=False)

ALLOWED_HOSTS = env("ALLOWED_HOSTS", default=[])

database_url = env('DATABASE_URL')
DATABASES = {
    'default': dj_database_url.parse(database_url)
}
