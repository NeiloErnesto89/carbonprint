"""
Django settings for carbonsite project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
# secret key test
# from os import path
# if path.exists("env.py"):
#   import env

# via python package python-dotenv to access env variables
from dotenv import load_dotenv

load_dotenv()

# https://dev.to/vladyslavnua/how-to-protect-your-django-secret-and-oauth-keys-53fl 
# this works and prints dummy key
SECRET_KEY = str(os.getenv('SECRET_KEY'))
# print(SECRET_KEY) # this works and prints dummy key

# SECURITY WARNING: keep the secret key used in production secret!

# SECRET_KEY = os.environ.get('SECRET_KEY')
# print(SECRET_KEY + " is the secret key")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jmc=c)%-v-ig-dkpr%yt@npn8@e9)9$)t53kwwnk22t^)2_o0m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions', # temp sesh on server for managing user data - legacy
    'django.contrib.messages',  # one time msg to user
    'django.contrib.staticfiles', # serving static files e.g. images, css, js
    'home',
    'debug_toolbar', # django debug toolbar
    'notes',
    'members', # users app
    'weather',
    'crispy_forms', # django crispy forms
    'crispy_bootstrap4', # django crispy forms bootstrap 4
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware', # django debug toolbar
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

# django debug toolbar - local ip address
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

ROOT_URLCONF = 'carbonsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'static/templates'], # add templates folder to project
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

WSGI_APPLICATION = 'carbonsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [ 
    BASE_DIR / 'static', # add static folder to project
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # path to dir where we want django to store uploaded files - stored on filesystem not db for performance
MEDIA_URL = '/media/' # url to access files in browser

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'


