import os
from distutils.util import strtobool

from dotenv import load_dotenv


load_dotenv()


VERSION: str = "0.1.0"

INSTALLED_APPS: list[str] = [
    "users",
]

DEBUG: bool = bool(strtobool(os.environ.get("DEBUG", "False")))

# CORS
CORS_ALLOWED_METHODS: list[str] = os.environ.get("CORS_ALLOWED_METHODS", "*").split(",")
CORS_ALLOWED_HEADERS: list[str] = os.environ.get("CORS_ALLOWED_METHODS", "*").split(",")
CORS_ALLOWED_HOSTS: list[str] = os.environ.get("CORS_ALLOWED_HOSTS", "").split(",")


# Database
DB_HOST: str = os.environ.get("DB_HOST")
DB_NAME: str = os.environ.get("DB_NAME")
DB_USER: str = os.environ.get("DB_USER")
DB_PORT: str = os.environ.get("DB_PORT", "5432")
DB_PASSWORD: str = os.environ.get("DB_PASSWORD")
