"""
WSGI config for WebSearchableEquipmentDatabase project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/opt/mswebapp/WebSearchableEquipmentDatabase')

sys.path.append('/opt/anaconda3/envs/mswebapp/lib/python3.8/site-packages')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebSearchableEquipmentDatabase.settings')

application = get_wsgi_application()
