"""
# Name:           meas/settings.py
# Description:
# Created by:     Auto
# Date Created:   Oct 07 2016
# Last Modified:  Oct 07 2016
# Modified by:    Phuc Le-Sanh
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ["MEAS_SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Web application
    'webapp.apps.WebAppConfig',

    # Models
    'meas_models.apps.MeasModelsConfig', 

    # Haystack
    'drf-haystack',
    # 'haystack',
    # 'whoosh',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'meas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'meas.wsgi.application'

# Whoosh
# PROJECT_DIRECTORY = os.getcwd() 
# WHOOSH_INDEX = os.path.join(PROJECT_DIRECTORY,'../whoosh/')

# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
#     },
#     'db': {
#         'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
#     },
# }

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ["MEAS_DATABASE_NAME"],
        'USER': os.environ["MEAS_DATABASE_USER"],
        'PASSWORD': os.environ["MEAS_DATABASE_PASSWORD"]
    }
}


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'