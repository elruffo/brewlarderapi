"""
Django settings for brewlarderapi project on Heroku. Fore more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


# Application definition

INSTALLED_APPS = (

    # default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # local apps
    'backoffice',
    'frontoffice',

    # third party apps
    'rest_framework',
    'corsheaders',
    # 'bootstrap_django_tags',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'brewlarderapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', ],
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

WSGI_APPLICATION = 'brewlarderapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# Internationalization and localization
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Rome'  # 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# LOCALE_PATHS = BASE_DIR + '/locale'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DEFAULT_LOG_LEVEL = 'WARNING'

_HANDLERS = {
    'console': {
        'level': DEFAULT_LOG_LEVEL,
        'formatter': 'default',
        'class': 'logging.StreamHandler'
    },
}

LOG_FORMAT = '[%(levelname)s %(asctime)s %(name)s %(module)s: %(processName)s] %(message)s'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': LOG_FORMAT
        }
    },
    'handlers': _HANDLERS,
    'loggers': {
        'django': {
            'level': DEFAULT_LOG_LEVEL,
        },
        'custom': {
            'level': DEFAULT_LOG_LEVEL,
        },
    },
    'root': {
        'handlers': _HANDLERS.keys(),
        'level': DEFAULT_LOG_LEVEL,
    }
}

# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }

CORS_ORIGIN_WHITELIST = (
    'brewlarderclient.herokuapp.com',
)

# CORS_ORIGIN_ALLOW_ALL = True

BREWERYDB_API_KEY = os.environ.get("BREWERYDB_API_KEY")
if not BREWERYDB_API_KEY:
    # TODO: raise error for missing BREWERYDB_API_KEY
    pass


# Loading test/prod settings based on ENV settings
ENV = os.environ.get('ENV', 'local')
if ENV == 'prod':
    try:
        from production_settings import *
    except ImportError:
        pass
