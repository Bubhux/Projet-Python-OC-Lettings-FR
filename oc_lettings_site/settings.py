import os
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

# Affiche le contenu de SENTRY_DSN (pour débogage)
# Décommenter pour vérifier la clé "SENTRY_DSN"
# print("SENTRY_DSN:", SENTRY_DSN)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.99.100', f'{HEROKU_APP_NAME}.herokuapp.com']

# Initialisation de Sentry
sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[
        DjangoIntegration(
            transaction_style='url',
            middleware_spans=True,
            signals_spans=False,
            cache_spans=False,
        ),
    ],
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
    },
    'root': {
        'handlers': ['sentry', 'console'],  # Utilisez à la fois Sentry et la console
        'level': 'DEBUG',                   # Niveau de logging minimum global (peut être ajusté)
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
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'oc-lettings-site.sqlite3'),
    }
}

# Récupérer les paramètres de connexion de la base de données à partir de DATABASE_URL
# Définis une durée maximale de connexion de 600 secondes.
# Exige le chiffrement SSL pour les connexions à la base de données.
check_db_config = dj_database_url.config(conn_max_age=600, ssl_require=True)

# Mettre à jour la configuration de la base de données existante avec les paramètres récupérés
DATABASES['default'].update(check_db_config)


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
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
