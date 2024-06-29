import os
from pathlib import Path
from ruamel.yaml import YAML

BASE_DIR = Path(__file__).resolve().parent.parent

yaml_file = BASE_DIR / 'chatterbot_settings.yaml'
yaml = YAML(typ='safe')

if os.path.exists(yaml_file):
    with open(yaml_file, 'r', encoding='utf-8') as file:
        chatterbot_settings = yaml.load(file)
else:
    chatterbot_settings = {}

SECRET_KEY = chatterbot_settings.get('secret_key', 'your_secret_key_here')
DEBUG = chatterbot_settings.get('debug', True)
ALLOWED_HOSTS = chatterbot_settings.get('allowed_hosts', [])
LINE_CHANNEL_ACCESS_TOKEN = chatterbot_settings.get('LINE_CHANNEL_ACCESS_TOKEN', '')
LINE_CHANNEL_SECRET = chatterbot_settings.get('LINE_CHANNEL_SECRET', '')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'your_project_line',  # 確保你的應用程式名稱正確
    'django_chatterbot',
    'chatterbot_app.apps.ChatterbotAppConfig',
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

ROOT_URLCONF = 'your_project_line.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 如果有自定義模板，加入此處
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

WSGI_APPLICATION = 'your_project_line.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'zh-Hant'
TIME_ZONE = 'Asia/Taipei'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CHATTERBOT = chatterbot_settings.get('chatterbot', {})
