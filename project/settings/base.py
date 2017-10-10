"""
Django settings for GAE project.
"""

# Setup Djangae at beginning
from djangae.settings_base import *
from django.core.urlresolvers import reverse_lazy


# Base dir
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Debug settings
from ..boot import get_app_config
SECRET_KEY = get_app_config().secret_key
DEBUG = True


INSTALLED_APPS = (
    'djangae',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'djangae.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'csp',
    'cspreports',
    'djangae.contrib.gauth_datastore',
    'djangae.contrib.security',
    'django_extensions',
    'rest_framework',
    'project',
)


MIDDLEWARE_CLASSES = (
    'djangae.contrib.security.middleware.AppEngineSecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'djangae.contrib.gauth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'csp.middleware.CSPMiddleware',
    # Standard Django CSRF middleware supports sessions since 1.11
    # We prepare to use it over session_csrf for DRF
    # We use it for protecting website forms
    'django.middleware.csrf.CsrfViewMiddleware',
    # DRF is a requirement for Djangae and it is required to be installed
    # for Djangae manage.py client
    'session_csrf.CsrfMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                # We would like to use standard CSRF processor for website content
                # 'session_csrf.context_processor',
            ],
            'debug': True,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]


# Checks
SILENCED_SYSTEM_CHECKS = [
    'security.W003',
]
from ..boot import register_custom_checks
register_custom_checks()


# Routing
ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'


# Language settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static settings
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# CSRF
# Configure standard CSRF as session_csrf
CSRF_USE_SESSIONS = True


# CSP
CSP_REPORT_URI = reverse_lazy('report_csp')
CSP_REPORTS_LOG = True
CSP_REPORTS_LOG_LEVEL = 'warning'
CSP_REPORTS_SAVE = True
CSP_REPORTS_EMAIL_ADMINS = False


CSP_DEFAULT_SRC = ("'self'", "*.gstatic.com")
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", "fonts.googleapis.com", "*.gstatic.com")
CSP_FONT_SRC = ("'self'", "themes.googleusercontent.com", "*.gstatic.com")
CSP_FRAME_SRC = ("'self'", "www.google.com", "www.youtube.com", "accounts.google.com", "apis.google.com", "plus.google.com", "*.hotjar.com")
CSP_SCRIPT_SRC = ("'self'", "'unsafe-eval'", "'unsafe-inline'", "*.googleanalytics.com", "*.hotjar.com", "*.google-analytics.com", "ajax.googleapis.com")
CSP_IMG_SRC = ("'self'", "data:", "s.ytimg.com", "*.googleusercontent.com", "*.gstatic.com", "www.google-analytics.com")
CSP_CONNECT_SRC = ("'self'", "plus.google.com", "www.google-analytics.com", "*.coinmarketcap.com", "*.hotjar.com", "*.infura.io")


# Rest settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}


# Auth settings
# Standard user auth model is preferred one over djangae
AUTHENTICATION_BACKENDS = (
    # 'djangae.contrib.gauth_datastore.backends.AppEngineUserAPIBackend',
    'django.contrib.auth.backends.ModelBackend',
)
LOGIN_REDIRECT_URL = 'admin'
