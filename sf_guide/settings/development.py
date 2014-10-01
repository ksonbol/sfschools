from common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$o_i1r+x8+oux!h41-x+k(-+)#giijyn23h6@h#ur&mq06rbd$'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sf_guide_dev',
        'USER': 'sf_guide',
        'PASSWORD': 'TgVmdLevPbykfERp'
    }
}
