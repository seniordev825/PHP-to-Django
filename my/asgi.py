"""
ASGI config for my project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my.settings')

application = get_asgi_application()
