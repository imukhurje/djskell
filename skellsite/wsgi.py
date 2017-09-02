"""
WSGI config for skellsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
import site

site.addsitedir('/home/ubuntu/.virtualenvs/skellenv/lib/python3.4/site-packages')
sys.path.append('/var/www/django_projects/skellsite')
sys.path.append('/var/www/django_projects/skellsite/skellsite')

activate_env=os.path.expanduser("/home/ubuntu/.virtualenvs/skellenv/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skellsite.settings")

application = get_wsgi_application()
