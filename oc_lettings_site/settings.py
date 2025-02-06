import os
import sys
import sentry_sdk
import dj_database_url

from sentry_sdk.integrations.django import DjangoIntegration
from decouple import config
from django.core.management.utils import get_random_secret_key


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Chargement des variables d'environnement depuis le fichier .env
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY', default=get_random_secret_key())
SENTRY_DSN = config('SENTRY_DSN', default='')
HEROKU_APP_NAME = config('HEROKU_APP_NAME', default='')
RAILWAY_APP_NAME = config('RAILWAY_APP_NAME', default='')
RAILWAY_TOKEN = config('RAILWAY_TOKEN', default='')
RAILWAY_SERVICE_ID = config('RAILWAY_SERVICE_ID', default='')
RAILWAY_PROJECT_ID = config('RAILWAY_PROJECT_ID', default='')
DEBUG = config('DEBUG', default=False, cast=bool)

# Affiche le contenu de SENTRY_DSN (pour débogage)
# Décommenter pour vérifier la clé "SENTRY_DSN"
# print("SENTRY_DSN:", SENTRY_DSN)

# Chargement de l'environnement avant d'utiliser `DEBUG`
ENVIRONMENT = config('ENVIRONMENT', default='development')

if ENVIRONMENT == 'development':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = [
    '0.0.0.0',
    'localhost',
    '127.0.0.1',
    'oc-lettings-apps-production.up.railway.app',
    f'{HEROKU_APP_NAME}.herokuapp.com'
]

ALLOWED_HOSTS = [host for host in ALLOWED_HOSTS if host]  # Supprime les entrées vides

CSRF_TRUSTED_ORIGINS = ["https://oc-lettings-apps-production.up.railway.app"]

# Initialisation de Sentry (uniquement si `collectstatic` n'est pas exécuté)
if 'collectstatic' not in sys.argv:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True
    )

# Configuration du modèle de logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'sentry': {
            'level': 'ERROR',  # Niveau de logging minimum à envoyer à Sentry
            'class': 'sentry_sdk.integrations.logging.EventHandler',
        },
        'console': {
            'level': 'DEBUG',  # Niveau de logging minimum à afficher dans la console
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
        },
    },
    'root': {
        # Utilisez à la fois Sentry, la console et un fichier de log
        'handlers': ['sentry', 'console', 'file'],
        # Niveau de logging minimum global (peut être ajusté)
        'level': 'DEBUG',
    },
}

# Application definition
INSTALLED_APPS = [
    'oc_lettings_site.apps.OCLettingsSiteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lettings',
    'profiles',
]

# Si l'environnement est en production, utilisez Whitenoise, sinon StaticFilesStorage
if ENVIRONMENT == 'production':
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    # Ajoutez WhiteNoise dans les middleware
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
else:
    # En développement, utiliser StaticFilesStorage par défaut
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

ROOT_URLCONF = 'oc_lettings_site.urls'

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

WSGI_APPLICATION = 'oc_lettings_site.wsgi.application'

# Configuration du modèle de clé primaire automatique par défaut
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{os.path.join(BASE_DIR, 'oc-lettings-site.sqlite3')}"
    )
}

# Si DATABASE_URL est défini dans l'environnement, il l'utilise, sinon utilise SQLite
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(default=os.environ['DATABASE_URL'])


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
