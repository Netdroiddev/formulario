# settings.py - Configuración Django
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-^$e!z0#&r1!hx$+b)r4@6$6f@7e8!*v5@2^!7$6f@7e8!*v5@2'  # Cambia esto en producción!

DEBUG = True  # Cambiar a False en producción

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registro_empleados',  # Tu aplicación
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'configuracion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',  # Para acceso a MEDIA_URL
            ],
        },
    },
]

WSGI_APPLICATION = 'configuracion.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuración crítica para archivos estáticos y multimedia
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Directorio para archivos estáticos

MEDIA_URL = '/media/'  # URL base para archivos multimedia
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Ruta física en el sistema de archivos

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de tamaño máximo para subida de imágenes (opcional)
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5 MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5 MB



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Motor de la base de datos
        'NAME': 'FIRMAS',                # Nombre de tu base de datos
        'USER': 'root',                 # Usuario de la base de datos
        'PASSWORD': 'Camelo10@#*',          # Contraseña del usuario
        'HOST': '69.197.142.191',                  # Dirección del servidor (localhost si es local)
        'PORT': '3306',                       # Puerto de la base de datos (3306 por defecto)
        },
 }
