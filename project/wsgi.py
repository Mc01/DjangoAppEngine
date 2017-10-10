from .boot import fix_path
fix_path()

import os
from django.core.wsgi import get_wsgi_application
from djangae.environment import is_production_environment
from djangae.wsgi import DjangaeApplication


settings = 'project.settings.production' if is_production_environment() else 'project.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
application = DjangaeApplication(get_wsgi_application())
