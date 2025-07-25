from pathlib import Path

# Importing os for multiple use
import os

# For Dotenv file
from dotenv import load_dotenv
load_dotenv()

# Simplifying
hidden = os.environ










# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = hidden.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # Installed Rest_Framework
    'rest_framework',

    # JWT Authentication
    'rest_framework_simplejwt',

    # Cors
    'corsheaders',

    # Installed Apps
    'user',
    'listing'
]

MIDDLEWARE = [
    # Cors Middleware
    'corsheaders.middleware.CorsMiddleware',


    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Apato.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Apato.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# PostgreSQL for database
DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # PostgreSQL
        'NAME': hidden.get('DB_NAME'), # Custome Name
        'USER': hidden.get('DB_USER'), # Default User
        'PASSWORD': hidden.get('DB_PASSWORD'), # User pasword
        'HOST': hidden.get('DB_HOST'), # Custom Host
        'PORT': hidden.get('DB_PORT'), # Customize port
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Cors allow Origin
CORS_ALLOW_ALL_ORIGINS = True # for development allowing allowing from all origin


# Using Custom User
AUTH_USER_MODEL = 'user.User' # app_name.calss_name


# For Images the static files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Rest Framewrok settings
REST_FRAMEWORK = {
    # For Cursor Paginatin
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination',

    # For JWT authentication
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
