"""
Django settings for try_token project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '72#jc)ljx@)@qvx_av9fc=i%jxtwe0g=t)bplo0j)@_as7t5!9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#利於使用ngrok測試
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #rest auth setting
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    
    #rest auth Registration
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',

    #第三方登入 facebook
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',

    'test_token',
    'django_filters', #自定義過濾器
]
# rest-auth registration setting
SITE_ID = 1


#=================django-restframework-jwt=======================
# #設定token時效
import datetime

JWT_AUTH = {
    #允不允許重新刷新
    'JWT_ALLOW_REFRESH': True,

    #失效時間(有動還是會失效)
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=30),
    #失效時間(都不動的話)
    # 'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=10),
}
#=================django-restframework-jwt=======================


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'try_token.urls'

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

            ],
        },
    },
]

WSGI_APPLICATION = 'try_token.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'social_auth_test',
        'USER': 'root',
        'PASSWORD': 'April29love',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        #第三方登入。。。。不設定migration會出錯
        'OPTIONS': {'init_command': 'SET default_storage_engine=INNODB;'}
    },
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'test_token.User'

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL= '/media/'
MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')

# 如果會發生Timeout的事情，要先檢查網路是否正常
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'jmm.chang@gmail.com'
EMAIL_HOST_PASSWORD = '88455488'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

#讓第三方登入重新導向login頁面
LOGIN_REDIRECT_URL = '/login'

#讓user一定要填email
ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = "mandatory"

REST_USE_JWT = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
            'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

# after confirming email , redirect urlF
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/login'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]