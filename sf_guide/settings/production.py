from common import *
from getenv import env

# Parse database configuration from $DATABASE_URL
import dj_database_url

DATABASES = {}
DATABASES['default'] =  dj_database_url.config()
SECRET_KEY = env('SECRET_KEY')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

STATIC_ROOT = 'staticfiles'

DEBUG = True
TEMPLATE_DEBUG = False

