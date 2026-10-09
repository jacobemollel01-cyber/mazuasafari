
"""
Django settings for mazua_safaris project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# --------------------------------------------------
# Project paths and environment variables
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from the project root .env file
load_dotenv(BASE_DIR / ".env")

# --------------------------------------------------
# Security settings
# --------------------------------------------------

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "")

DEBUG = os.environ.get("DJANGO_DEBUG", "True").lower() == "true"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

# --------------------------------------------------
# Applications
# --------------------------------------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "website",
]

# --------------------------------------------------
# Middleware
# --------------------------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mazua_safaris.urls"

# --------------------------------------------------
# Templates
# --------------------------------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mazua_safaris.wsgi.application"

# --------------------------------------------------
# Database
# --------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# --------------------------------------------------
# Password validation
# --------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# --------------------------------------------------
# Internationalization
# --------------------------------------------------

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"

USE_I18N = True
USE_TZ = True

# --------------------------------------------------
# Static files
# --------------------------------------------------

STATIC_URL = "static/"

# --------------------------------------------------
# Email configuration — Django 6.1
# --------------------------------------------------

ADMIN_NOTIFICATION_EMAIL = os.environ.get(
    "ADMIN_NOTIFICATION_EMAIL",
    "mazuarobert@gmail.com",
)

# Django 6.1 uses MAILERS here.
# Do not define EMAIL_HOST_USER or EMAIL_HOST_PASSWORD
# as Django settings; read them directly from the environment.

MAILERS = {
    "default": {
        "BACKEND": "django.core.mail.backends.smtp.EmailBackend",
        "OPTIONS": {
            "host": "smtp.gmail.com",
            "port": 587,
            "username": os.environ.get("EMAIL_HOST_USER", ""),
            "password": os.environ.get("EMAIL_HOST_PASSWORD", ""),
            "use_tls": True,
        },
    },
}

# --------------------------------------------------
# Default primary key
# --------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"