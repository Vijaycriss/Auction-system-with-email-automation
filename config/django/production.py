from .base import *
from config.env import env



SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=False)

#ALLOWED_HOSTS = env("ALLOWED_HOSTS", default=[])

