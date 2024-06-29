# chatterbot_app/chatterbot.py

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.ext.django_chatterbot import settings as chatterbot_settings
from chatterbot.ext.django_chatterbot import utils

# Load ChatterBot settings from YAML file
chatbot = ChatBot(
    'Django ChatterBot',
    **utils.initialize()
)

# Optionally, train the bot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    chatterbot_settings.get('training')
)
