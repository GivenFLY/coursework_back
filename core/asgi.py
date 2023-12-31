"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

import dotenv
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

application = get_asgi_application()
