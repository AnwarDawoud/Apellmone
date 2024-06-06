# settings.py
import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _

load_dotenv()

# Base directory of the Django project
BASE_DIR = Path(__file__).resolve().parent.parent


# Secret key for Django application
SECRET_KEY = os.getenv('SECRET_KEY')

# Directory where Django will look for templates
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# Determine if running on Heroku based on environment variable
ON_HEROKU = os.getenv('ON_HEROKU', default='False').lower() == 'true'

# Set DEBUG to False if running on Heroku
if ON_HEROKU:
    DEBUG = False
else:
    DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'core',  # Add your app here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # LocaleMiddleware should be here
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Apellmone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'core', 'templates', 'core'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'Apellmone.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

GNU_GETTEXT_TOOLKIT_PATH = 'C:\\Program Files\\gettext\\bin'

GNU_TRANSLATE = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

LANGUAGE_CODE = 'uk'  # Default language code
LANGUAGES = [
    ('en', _('English')),
    ('uk', _('Ukrainian')),
    # Add more languages if needed
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),  # Directory where translation files will be stored
]

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'core', 'static', 'core'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LANGUAGE_COOKIE_NAME = 'django_language'
