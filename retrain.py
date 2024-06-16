# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 14:38:57 2024

@author: 88693
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import sqlite3

# 建立 ChatterBot
chatbot = ChatBot('LearningBot')

# 連接到資料庫並獲取對話數據
conn = sqlite3.connect('chatbot_data.db')
cursor = conn.cursor()
cursor.execute("SELECT user_input, bot_response FROM conversations")
conversations = cursor.fetchall()
conn.close()

# 重新訓練模型
trainer = ListTrainer(chatbot)
for conversation in conversations:
    trainer.train([conversation[0], conversation[1]])

# 保存模型
chatbot.storage.drop()
chatbot.storage.create()
