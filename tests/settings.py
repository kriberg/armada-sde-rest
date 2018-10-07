import os
import environ



TIME_ZONE = 'UTC'
USE_TZ = True
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_URL = '/static/'
STATIC_ROOT = ''
MEDIA_ROOT = ''
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
}]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)
env = environ.Env()
environ.Env.read_env()
DEBUG = env('DEBUG', default=False)
SECRET_KEY = env('SECRET_KEY', default='hunter2')
ROOT_URLCONF = 'tests.urls'
DATABASES = {
    'default': env.db(default='psql://postgres@localhost/sde'),
}
CACHES = {
    'default': env.cache(default='dummycache://'),
}

ARMADA = {
    'SDE': {
        'schema': 'test'
    }
}

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.staticfiles',
    'rest_framework',
    'armada_sde',
    'armada_sde_rest',
    'tests.testapp',
]
