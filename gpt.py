# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 03:42:51 2024

@author: 88693
"""

import sqlite3

# 創建資料庫並創建表格
conn = sqlite3.connect('chatbot_data.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS conversations (user_input TEXT, bot_response TEXT)''')
conn.commit()
conn.close()

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    bot_response = chatbot.get_response(user_message)

    # 存儲對話數據
    conn = sqlite3.connect('chatbot_data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO conversations (user_input, bot_response) VALUES (?, ?)", (user_message, str(bot_response)))
    conn.commit()
    conn.close()

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=str(bot_response))
    )
