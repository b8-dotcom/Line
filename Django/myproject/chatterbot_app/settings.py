import os
from ruamel.yaml import YAML

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load chatterbot settings from YAML
CHATTERBOT_SETTINGS_FILE = os.path.join(BASE_DIR, 'path_to_your_chatterbot_settings/chatterbot_settings.yaml')

yaml = YAML(typ='safe')

with open(CHATTERBOT_SETTINGS_FILE, 'r', encoding='utf-8') as f:
    chatterbot_settings = yaml.load(f)

SECRET_KEY = chatterbot_settings.get('secret_key', 'django-insecure-@^l38*7mq8@d0i@$6=^v==&y8)t#pdw7_nbvva1542u8&4b0ra')
DEBUG = chatterbot_settings.get('debug', True)
ALLOWED_HOSTS = chatterbot_settings.get('allowed_hosts', ['localhost', '127.0.0.1', '[::1]'])

chatterbot_config = chatterbot_settings.get('chatterbot', {})

CHATTERBOT = {
    'name': chatterbot_config.get('name', {
        'zh': '林家水果行',
        'en': 'Fruit Shop Lin',
        'ja': '林家フルーツ店',
        'ko': '린 과일 가게'
    }),
    'logic_adapters': chatterbot_config.get('logic_adapters', [
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': {
                'zh': '非常抱歉，我未能理解您的意思。',
                'en': 'I apologize, I didn\'t quite understand your meaning.',
                'ja': '申し訳ありませんが、私はあなたの要求を理解できませんでした。',
                'ko': '죄송합니다, 요청을 이해하지 못했습니다.'
            },
            'maximum_similarity_threshold': 0.9
        }
    ]),
    'international_data': chatterbot_config.get('international_data', [])
}

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

# LINE Bot settings
LINE_CHANNEL_ACCESS_TOKEN = chatterbot_settings.get('line_bot', {}).get('channel_access_token', '')
LINE_CHANNEL_SECRET = chatterbot_settings.get('line_bot', {}).get('channel_secret', '')
