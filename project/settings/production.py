from .base import *


# Turn off debug
DEBUG = False


# Security settings
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 2592000  #30 days
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True

PREPEND_WWW = True

SECURE_REDIRECT_EXEMPT = [
    # App Engine doesn't use HTTPS internally, so the /_ah/.* URLs need to be exempt.
    # Django compares these to request.path.lstrip("/"), hence the lack of preceding /
    r'^_ah/',
]


FILE_UPLOAD_MAX_MEMORY_SIZE = 52428800


# Add the cached template loader for the Django template system (not for Jinja)
for template in TEMPLATES:
    template['OPTIONS']['debug'] = False
    if template['BACKEND'] == 'django.template.backends.django.DjangoTemplates':
        template['OPTIONS']['loaders'] = [
            ('django.template.loaders.cached.Loader', template['OPTIONS']['loaders'])
        ]
