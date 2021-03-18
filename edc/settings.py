import os
from pathlib import Path

import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_DIR = str(Path(os.path.join(BASE_DIR, ".env")))

env = environ.Env(
    DJANGO_DEBUG=(bool, False),
    DEBUG_TOOLBAR=(bool, False),
    DJANGO_EDC_BOOTSTRAP=(int, 3),
    DATABASE_SQLITE_ENABLED=(bool, False),
    DJANGO_AUTO_CREATE_KEYS=(bool, False),
    DJANGO_CRYPTO_FIELDS_TEMP_PATH=(bool, False),
    DJANGO_CSRF_COOKIE_SECURE=(bool, True),
    SIMPLE_HISTORY_PERMISSIONS_ENABLED=(bool, False),
    SIMPLE_HISTORY_REVERT_DISABLED=(bool, False),
)

environ.Env.read_env(ENV_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_DEBUG")
DEBUG_TOOLBAR = env("DEBUG_TOOLBAR")

SUBJECT_DATA_MODEL = env("EDC_SUBJECT_DATA_MODEL")

LOGIN_REDIRECT_URL = env.str("DJANGO_LOGIN_REDIRECT_URL")

EDC_THEME = env("EDC_THEME")

EDC_THEME_MODE = env("EDC_THEME_MODE")

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django_crypto_fields.apps.AppConfig",
    "edc_auth.apps.EdcAuthConfig",
    "edc_dashboard.apps.EdcDashboardConfig",
    "edc_sites.apps.EdcSitesConfig",
    "edc_navbar.apps.EdcNavbarConfig",
    "edc_forms.apps.EdcFormsConfig",
    "edc_models.apps.EdcModelsConfig",
    "edc_theme.apps.EdcThemeConfig",
    "edc_crfs.apps.EdcCrfsConfig",
    "django_revision.apps.AppConfig",
    "django_audit_fields.apps.AppConfig",
    "simple_history",
    "preventconcurrentlogins",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_currentuser.middleware.ThreadLocalUserMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
    "preventconcurrentlogins.middleware.PreventConcurrentLoginsMiddleware",
]

# setting debug toolbar
if DEBUG and DEBUG_TOOLBAR:
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
    INTERNAL_IPS = ["127.0.0.1"]

ROOT_URLCONF = "edc.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

ETC_DIR = env.str("DJANGO_ETC_FOLDER")

WSGI_APPLICATION = "edc.wsgi.application"
# django_simple_history
SIMPLE_HISTORY_PERMISSIONS_ENABLED = env.str("SIMPLE_HISTORY_PERMISSIONS_ENABLED")
SIMPLE_HISTORY_REVERT_DISABLED = env.str("SIMPLE_HISTORY_REVERT_DISABLED")

# django_crypto_fields
KEY_PATH = env.str("DJANGO_KEY_FOLDER")
AUTO_CREATE_KEYS = env("DJANGO_AUTO_CREATE_KEYS")
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Django field class to your models to track the git revision with every model instance saved.
# https://pypi.org/project/django-revision/

GIT_DIR = BASE_DIR

APP_NAME = env.str("DJANGO_APP_NAME")

ACCOUNT_EMAIL_VERIFICATION = "none"

LOGIN_REDIRECT_URL = "home"

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"

EDC_BOOTSTRAP = env("DJANGO_EDC_BOOTSTRAP")
