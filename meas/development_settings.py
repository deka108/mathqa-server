
"""
# Name:           meas/settings.py
# Description:
# Created by:     Phuc Le-Sanh
# Date Created:   Oct 10 2016
# Last Modified:  Nov 23 2016
# Modified by:    Phuc Le-Sanh
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'g(yej*3clhw8mh1lge2jd*f7h0uam9exedd$ya50n-^n1#p2(9'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'fontawesome',
    'autofixture',
    'ckeditor',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',

    # Web application
    'webapp.apps.WebAppConfig',

    # Models
    'meas_models.apps.MeasModelsConfig',

    # CMS
    'cms.apps.CmsConfig',

    # Common
    'meas_common.apps.MeasCommonConfig',

    # API
    'api.apps.ApiConfig',
    'apiv2.apps.Apiv2Config',

    # Search
    'search.apps.SearchConfig',

    # Import Export
    'import_export',

    # Haystack
    # 'drf-haystack',
    'haystack',
    # 'whoosh_index',

    # Django-Extensions
    'django_extensions',

    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
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

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'if-modified-since'
)

CSRF_TRUSTED_ORIGINS = (
    'localhost:8080',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
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

# Whoosh
WHOOSH_INDEX = os.path.join(BASE_DIR, 'whoosh_index')

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': WHOOSH_INDEX,
    },
}

WSGI_APPLICATION = 'meas.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'meas_development',
        'USER': 'root',
        'PASSWORD': '123456'
    },
}

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

LOGOUT_REDIRECT_URL = '/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': [
                'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-',
                'Templates']},
            {'name': 'clipboard', 'items': [
                'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-',
                'Undo', 'Redo']},
            {'name': 'editing', 'items': [
                'Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea',
                       'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
                       'Superscript', '-', 'ReplacemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent',
                       'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight',
                       'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley',
                       'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': [
                'Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',
            {'name': 'yourcustomtools', 'items': [
                'Preview',
                'Mathjax',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',
        'toolbarGroups': [{'name': 'document', 'groups': ['mode', 'document',
                                                          'doctools']}],
        'height': 291,
        'width': '100%',
        'filebrowserWindowHeight': 725,
        'filebrowserWindowWidth': 940,
        'toolbarCanCollapse': True,
        'mathJaxLib': '//cdn.mathjax.org/mathjax/latest/' +
        'MathJax.js?config=TeX-MML-AM_CHTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                'devtools',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath',
                'mathjax'
            ]),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',),

    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
}
