"""
Django settings for doc_appoint project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
temp_dir = os.path.join(BASE_DIR,'templates')
static_dir = os.path.join(BASE_DIR,'static')

MEDIA_URL = '/media/' 
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-08-n=$ulf#962m9clwhjin@k8ln50s4c1(nx&#9=s#kmn_^5i6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'role',
    'user',
    'ckeditor',
    'social_django',
    'division',
    'district',
    'station',
    'hospital_category',
    'hospital',
    'hospital_map',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

#celery
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


EMAIL_FILE_PATH = os.path.join(BASE_DIR,'static')


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER ='salmanmdsultan92@gmail.com'
EMAIL_HOST_PASSWORD = 'tffk jbwx xlfw pkzd'

ROOT_URLCONF = "doc_appoint.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [temp_dir],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'social_django.context_processors.backends',
            ],
        },
    },
]

WSGI_APPLICATION = "doc_appoint.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "doc_app_colaboration",
        "USER":"root",
        "PASSWORD": "Mahmud@100%",
        "HOST":"localhost",
        "PORT":3306
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [static_dir,]
LOGIN_URL = 'division_index'

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',  # Google authentication backend
    'django.contrib.auth.backends.ModelBackend',  # Default Django authentication backend
    # Add other authentication backends as needed
]

LOGIN_REDIRECT_URL = 'division_index'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1086434461459-619nsg12df35m5hfu2v8sp2pv4ctf7kr.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_PIPELINE = (
    # ... other pipeline steps ...
    'auth_user.pipeline.capture_social_auth_data',  # Add this line
    # ... other pipeline steps ...
)



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

