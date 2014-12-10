"""
Django settings for klaviaturregistret project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Import environment-specific settings.
from settings_local import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 2014-11-20 rollo: Moved to local_settings
#SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
# 2014-11-20 rollo: Moved to local_settings
#DEBUG = True

# 2014-11-20 rollo:
#TEMPLATE_DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ["klaviaturregistret.se", "www.klaviaturregistret.se"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'bootstrap3',
    'django.contrib.humanize',
    'web',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# SOCIAL_AUTH_FACEBOOK_KEY = ''
# SOCIAL_AUTH_FACEBOOK_SECRET = ''
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

ROOT_URLCONF = 'klaviaturregistret.urls'

WSGI_APPLICATION = 'klaviaturregistret.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# 2014-11-23 rollo: Moved to settings_local.py.
# DATABASES = {
#     'default': {
#         # 2014-11-20 rollo:
#         #'ENGINE': 'django.db.backends.sqlite3',
#         #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'klaviaturregistret',
#         'USER': 'klaviaturregistret',
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'sv-se'
LANGUAGES = (
     ('en', 'English'),
     ('sv', 'Swedish'),
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, os.pardir, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, os.pardir, 'media')

BOOTSTRAP3 = {
    'base_url': '//netdna.bootstrapcdn.com/bootstrap/3.3.1/',
}
