from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEFAULT_SECRET_KEY = ')@@ui9%belfbmv8=$^*kqpj$0v05l!xy)h5t*ux@71v=7@e^z7'
