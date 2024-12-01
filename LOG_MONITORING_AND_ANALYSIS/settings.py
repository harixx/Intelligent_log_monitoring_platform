"""
Django settings for LOG_MONITORING_AND_ANALYSIS project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Now you can access environment variables using os.getenv()
MONGODB_SETTINGS = {
    'host': os.getenv('mongodb+srv://mark:markmark003@atlascluster.ogqxvgo.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster'),
    'db': os.getenv('MONGODB_DB', 'windows')
}


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tp*9izdj+(rzpk0-^bn*y0kq4j4!3v7fab12ttd#@-ejcc(+5k'

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
    'rest_framework',
    'log_management_app',
    'user_management_app',
    'alerts_and_notifications_app',
    'AI_and_machine_learning_app',    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LOG_MONITORING_AND_ANALYSIS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'MainTemplates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LOG_MONITORING_AND_ANALYSIS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     },
   
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'log_database',
        'USER': 'mark',
        'PASSWORD': 'markmark003',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'logs',
#         'ENFORCE_SCHEMA': False,
#         'CLIENT': {
#             'host': 'mongodb+srv://mark:markmark003@atlascluster.ogqxvgo.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster',
#             'username': 'mark',
#             'password': 'markmark003',
#             'authMechanism': 'SCRAM-SHA-1',
#         },
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'user_management_app.User'


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/assets/files/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_ROOT = BASE_DIR / 'static/assets/files'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




MONGODB_SETTINGS = {
    'host': os.getenv('MONGODB_HOST', 'mongodb+srv://mark:markmark003@atlascluster.ogqxvgo.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster'),
    'db': os.getenv('MONGODB_DB', 'windows')
}


CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'