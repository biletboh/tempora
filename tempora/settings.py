"""
Django settings for tempora project.
"""

import os
import configparser
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

conf = configparser.ConfigParser()
conf.read(os.path.join(BASE_DIR, 'settings.ini'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = conf.get(
                    'tempora', 'secret',
                    fallback='8ze8kfn8@c!jat$*wryy+u@2^+1@ln27t5fql54qfq$2x$ac8x')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = conf.getboolean('tempora', 'debug', fallback = True)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # custom apps 
    'pbhouse.apps.PbhouseConfig',
    'users.apps.UsersConfig',
    'blog.apps.BlogConfig',
    'tags.apps.TagsConfig',

    # filebrowser and tinymce apps
    'grappelli',
    'filebrowser',
    'tinymce',

    # django core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # additionals apps
    'easy_thumbnails',
    'django_file_form',
    'django_file_form.ajaxuploader',
    'widget_tweaks',
    'el_pagination',
    'datetimewidget',
    'phonenumber_field',
]


SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tempora.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tempora.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

CURRDB = {'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3')}

if DEBUG is False:
    CURRDB = {  'ENGINE': 'django.db.backends.postgresql',
                'NAME': conf.get('tempora', 'dbname', fallback = 'tempora'),
                'USER': conf.get('tempora', 'dbuser', fallback = 'postgres'),
                'PASSWORD': conf.get(
                                    'tempora', 'dbpass',
                                    fallback = 'postgres'),
                'HOST': 'localhost',
                'PORT': '5432' }

DATABASES = {
    'default': CURRDB
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = (
        ('en', _('English')),
        ('uk', _('Ukrainian')),
        )

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
            os.path.join(BASE_DIR, 'locale'),
            )


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# allauth configuration

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_SIGNUP_FORM_CLASS = 'users.signupform.SignupForm'
AUTH_USER_MODEL = 'users.UserProfile'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = 'tempora.publ.house@gmail.com'
EMAIL_HOST_PASSWORD = 'TemporaFiliaVeritas'
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Tempora'

LOGIN_REDIRECT_URL = '/dashboard'


#Tumnails settings 

THUMBNAIL_ALIASES = {
    '': {
        'extra_small': {'size':(45, 45), 'crop': True},
        'small': {'size':(60, 60), 'crop': True},
        'big_avatar': {'size': (150, 150), 'crop': True},
        'preview': {'size': (250, 200), 'crop': True},
        'blog_first': {'size': (960, 720), 'crop': True},
        'blog_second': {'size': (400, 300), 'crop': True},
        'medium': {'size': (750, 450), 'crop': True},
        'large': {'size': (800, 450), 'crop': True},
        'extra_large': {'size': (1200, 600), 'crop': True},
        },
    }

THUMBNAIL_TRANSPARENCY_EXTENSION = 'png'


#TinyMCE config
TINYMCE_JS_URL = '/static/tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = '/static/tiny_mce'

TINYMCE_SPELLCHECKER = True
TINYMCE_DEFAULT_CONFIG = {
        'plugins': 'advlist,autolink,autoresize,emotions,fullpage,fullscreen,media,table,spellchecker,paste,searchreplace,wordcount',
        'theme': "advanced",
        'theme_advanced_resizing': True,
        'theme_advanced_resize_horizontal': True,
        'theme_advanced_buttons1': 'undo,redo,fontsizeselect,bold,italic,underline,strikethrough,|,forecolor,backcolor,|,bullist,numlist,|,justifyleft,justifycenter,justifyright,justifyfull,|,outdent,indent,|,link,unlink,|,image,media,|,emotions,blockquote,|,table,hr,sub,sup,charmap',
        'theme_advanced_buttons2' : "",
        'width': '100%',
        'cleanup_on_startup': True,
        'custom_undo_redo_levels': 10,
        }
TINYMCE_COMPRESSOR = False 
TINYMCE_FILEBROWSER = True 

