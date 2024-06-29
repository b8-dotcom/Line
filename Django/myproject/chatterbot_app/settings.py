import os
from ruamel.yaml import YAML

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load settings from YAML
SETTINGS_FILE = os.path.join(BASE_DIR, 'path_to_chatterbot_settings/chatterbot_settings.yaml')

yaml = YAML(typ='safe')

with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
    settings_data = yaml.load(f)

SECRET_KEY = settings_data.get('secret_key', 'django-insecure-@^l38*7mq8@d0i@$6=^v==&y8)t#pdw7_nbvva1542u8&4b0ra')
DEBUG = settings_data.get('debug', True)
ALLOWED_HOSTS = settings_data.get('allowed_hosts', ['localhost', '127.0.0.1', '[::1]'])

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Internationalization
LANGUAGE_CODE = 'zh-hant'
TIME_ZONE = 'Asia/Taipei'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Templates configuration
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

# Logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# LINE Bot settings (if defined in chatterbot_settings.yaml)
LINE_CHANNEL_ACCESS_TOKEN = settings_data.get('line_bot', {}).get('channel_access_token', '')
LINE_CHANNEL_SECRET = settings_data.get('line_bot', {}).get('channel_secret', '')
