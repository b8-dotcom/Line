# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 17:32:52 2024

@author: 88693
"""

# chatbot/bot.py
from chatterbot import ChatBot

# Create a new chat bot named 'FruitShopBot'
bot = ChatBot('FruitShopBot')

# Train the chat bot with some example statements
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train([
    '你好',
    '您好，有什麼可以為您效勞的呢?',
    '再見',
    '再見，祝您有美好的一天。',
    # Add more training data here
])
