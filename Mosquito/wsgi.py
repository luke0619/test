import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mosquito.settings')

application = get_wsgi_application()

from Mosquito.settings import DEBUG
if not DEBUG:
    from dj_static import Cling
    application = Cling(get_wsgi_application())