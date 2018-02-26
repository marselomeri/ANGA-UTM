"""
Django settings for ASTRAL_UTM project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['astral-utm.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    'pwa',

    'storages',

    'django.contrib.humanize',
    'djgeojson',

    'bootstrap3',
    'datetimewidget',
    'leaflet',

    'phonenumber_field',


    'organizations',
    'rpas',
    'accounts',
    'maps',
    'flight_plans',
    'applications',
    'weather',
    'utm_messages',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'ASTRAL_UTM.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'ASTRAL_UTM.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# add this
# import dj_database_url
# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)
# DATABASES['default']['CONN_MAX_AGE'] = 500


import dj_database_url
DATABASES['default'] = dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

GDAL_LIBRARY_PATH = os.getenv('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = os.getenv('GEOS_LIBRARY_PATH')


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE  = 'storages.backends.s3boto.S3BotoStorage'


LOGIN_URL = "accounts:login"
LOGIN_REDIRECT_URL = "rpas_list"

LEAFLET_CONFIG = {

    'DEFAULT_CENTER': (-1.5405, 36.6612),
    'DEFAULT_ZOOM': 9,
    'MAX_ZOOM': 17,
    'MIN_ZOOM':7,
    'SCALE': 'metric',
    'ATTRIBUTION_PREFIX': 'Astral Aerial Maps',

}

CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True

from ASTRAL_UTM.aws.conf import *


PWA_APP_NAME = 'Astral UTM'
PWA_APP_DESCRIPTION = "Keep It Simple, Stupid"
PWA_APP_THEME_COLOR = '#AA0F0F'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_START_URL = "/"
PWA_APP_ICONS = [

        {
        "src": 'https://s3.eu-west-2.amazonaws.com/astral-utm-bucket/static/favicons/android-icon-36x36.png',
        "sizes": "36x36"
        },
        {
        "src": 'https://s3.eu-west-2.amazonaws.com/astral-utm-bucket/static/favicons/android-icon-48x48.png',
        "sizes": "48x48"
        },
        {
        "src": 'https://s3.eu-west-2.amazonaws.com/astral-utm-bucket/static/favicons/android-icon-72x72.png',
        "sizes": "72x72"
        },
        {
        "src": 'https://s3.eu-west-2.amazonaws.com/astral-utm-bucket/static/favicons/android-icon-96x96.png',
        "sizes": "96x96"
        },
        {
         "src": 'https://s3.eu-west-2.amazonaws.com/astral-utm-bucket/static/favicons/android-icon-144x144.png',
         "sizes": "144x144"
        },
        {
            'src': 'https://s3.eu-west-2.amazonaws.com/astral-utm-bucket/static/favicons/192x192.png',
            'sizes': '192x192'
        },
        {
            'src': 'https://s3.eu-west-2.amazonaws.com/astral-utm-bucket/static/favicons/384x384.png',
            'sizes': '384x384'
        },
        {
            'src': 'https://s3.eu-west-2.amazonaws.com/astral-utm-bucket/static/favicons/512x512.png',
            'sizes': '512x512'
        }


]
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR,  'static/pwabuilder-sw.js')
