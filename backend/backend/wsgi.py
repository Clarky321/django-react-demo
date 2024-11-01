"""
Конфигурация WSGI для бэкенд-проекта.

Она представляет вызываемый WSGI как переменную уровня модуля с именем ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

application = get_wsgi_application()
