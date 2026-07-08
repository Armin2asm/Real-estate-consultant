from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# =====================
# BASIC SETTINGS
# =====================
SECRET_KEY = 'django-insecure-CHANGE-ME'
DEBUG = True
ALLOWED_HOSTS = []


# =====================
# APPS
# =====================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps
    'Agents',
    'Properties',
    'Accounts',
    'HomePage',
]
LOGIN_URL = "account:login"
LOGIN_REDIRECT_URL = "Home"
LOGOUT_REDIRECT_URL = "Home"


# =====================
# MIDDLEWARE
# =====================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # ✅ IMPORTANT FOR LANGUAGE SWITCH
    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =====================
# URLS
# =====================
ROOT_URLCONF = 'config.urls'


# =====================
# TEMPLATES
# =====================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# =====================
# DATABASE
# =====================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =====================
# INTERNATIONALIZATION (IMPORTANT)
# =====================
USE_I18N = True
USE_TZ = True

LANGUAGE_CODE = "en-us"
USE_I18N = False
LANGUAGES = [
    ("en", "English"),
]

LOCALE_PATHS = [
    BASE_DIR / "locale",
]


# =====================
# STATIC & MEDIA
# =====================
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'