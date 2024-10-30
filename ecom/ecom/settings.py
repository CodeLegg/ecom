from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()
# Paths
# ------------------------------------------------------------------------------
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Security Settings
# ------------------------------------------------------------------------------
# Keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-4ej6jn@x=^d#g8c8y+$+32$l)yi393-(36&+@@t0ue6j6t6^bh",  # Default for development
)

# Don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "") != "False"

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# Applications Installed
# ------------------------------------------------------------------------------
INSTALLED_APPS = [
    # Default Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Custom apps
    "store",  # Your custom app

    # Third-party apps
    "mptt",  # For hierarchical category management
    "django_mptt_admin",  # Admin integration for MPTT

    # Allauth (for authentication)
    "django.contrib.sites",  # Required by django-allauth
    "allauth",
    "allauth.account",  # For email/password authentication
    "allauth.socialaccount",  # For social authentication (Google, Facebook, etc.)
    "allauth.socialaccount.providers.google",  # Google OAuth
    "allauth.socialaccount.providers.facebook",  # Facebook OAuth
]

# Set the current site ID (required by allauth)
SITE_ID = 2


# Middleware
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Static file handling for production
    "allauth.account.middleware.AccountMiddleware",  # Required by allauth
]


# Authentication
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    "store.authentication_backends.EmailBackend",  # Custom email backend
    "django.contrib.auth.backends.ModelBackend",  # Default backend
    "allauth.account.auth_backends.AuthenticationBackend",  # Allauth backend
]

LOGIN_REDIRECT_URL = "/"  # Where to redirect users after login
LOGOUT_REDIRECT_URL = "/"  # Where to redirect users after logout

# Email backend for development (prints emails to the console)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Templates
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # Directories to search for templates
        "APP_DIRS": True,  # Allow automatic template discovery in app directories
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

# URL configuration
ROOT_URLCONF = "ecom.urls"

# WSGI Application
WSGI_APPLICATION = "ecom.wsgi.application"


# Database Configuration
# ------------------------------------------------------------------------------
# Use PostgreSQL in production or default to SQLite for development
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL", "sqlite:///db.sqlite3"),  # Use environment variable or fallback to SQLite
        conn_max_age=600,  # Optimize database connections for performance
    )
}


# Password Validation
# ------------------------------------------------------------------------------
# Validate the strength of user passwords
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# ------------------------------------------------------------------------------
# Language and timezone settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True  # Enable translation system
USE_TZ = True  # Enable timezone support


# Static Files
# ------------------------------------------------------------------------------
# URL to use when referring to static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"

# Directories where Django will look for static files
STATICFILES_DIRS = [BASE_DIR / "static"]  # Development

# The directory where static files will be collected for production
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise settings (for serving static files in production)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Media Files
# ------------------------------------------------------------------------------
# Media files (uploaded by users)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media/"


# Default primary key field type
# ------------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
