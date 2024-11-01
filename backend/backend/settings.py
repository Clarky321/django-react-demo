from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
import os

# Загружаемая переменная среды из файла .env
load_dotenv()

# Создание путей внутри проекта, таких как BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ для проекта Django (использовать другой для production)
SECRET_KEY = "django-insecure-^dd3gs$z3v^mdiftd#h74$su^f60=tg&au-fo@$o3p2s65&_sy"

# Отдалочный режим (Debug) только для разработки, на production устанавливается в False
DEBUG = True

# Разрешенные хосты для подключения (разрешен доступ с любого хоста)
ALLOWED_HOSTS = ["*"]

# Настройки REST Framework, используем JWT для аутентификации
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

# Настройки токенов JWT: время жизни токена доступа и обновления
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# Установленные приложения
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "api",  # Приложение api
    "rest_framework",  # Django REST Framework
    "corsheaders",  # CORS Headers для настройки кросс-доменных запросов
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # CORS Middleware для обработки кросс-доменных запросов
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Главный файл настроек URL
ROOT_URLCONF = "backend.urls"

# Настройки шаблонов Django
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Приложение WSGI
WSGI_APPLICATION = "backend.wsgi.application"

# Настройки базы данных
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # Движок базы данных SQLite
        "NAME": BASE_DIR / "db.sqlite3",  # Путь к файлу базы данных
    }
}

# Валидаторы паролей
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

# Настройки интернационализации
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Настройки статических файлов (например, css, изображения)
STATIC_URL = "static/"

# Тип поля по умолчанию для первичных ключей
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CORS настройки для разрешения всех источников
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWS_CREDENTIALS = True
