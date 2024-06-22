# -*- coding: utf-8 -*-
import sys
sys.path.append(r'C:\Users\88693\Documents\python\line\Django')
import os
import django
from django.conf import settings

# 設置 DJANGO_SETTINGS_MODULE 環境變量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_projec_line.settings')

# 確保 Django settings 被正確載入
django.setup()

# 現在可以導入其他 Django 相關的模組和函數了
from your_projec_line.models import Message

# 接下來可以繼續使用 Django 的其他功能

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.exceptions import InvalidSignatureError
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.storage.django_storage import DjangoStorageAdapter  # 引入 DjangoStorageAdapter
import logging
import time

app = Flask(__name__)

# LINE 設定
LINE_CHANNEL_ACCESS_TOKEN = '3N+hwqKvNK8MUNVrV4EeboNrD/1liUCyq30MZ241s1BDNKRie2hMywwMBquG72uqVFdQZqL+/TcqsO5sD2De5abt841S4Fb79Y0khqBCIe1jWsVW/JTxlabWkjoYdFfa8zcxOuPhJnjVIb3SJ+fhGwdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_SECRET = '93a8d88c1459c647e0a80e3ea21d95b8'

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# 設定日誌
logging.basicConfig(level=logging.INFO)

# 建立 ChatterBot 聊天機器人
chatbot = ChatBot(
    'LearningBot',
    storage_adapter='chatterbot.storage.django_storage.DjangoStorageAdapter',  # 使用 DjangoStorageAdapter
    django_app_name='your_projec_line'  # 替換成您的 Django 應用程式名稱
)

# 訓練繁體中文基本語料庫
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.chinese')  # 訓練繁體中文基本語料庫

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers.get('X-Line-Signature')
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.error("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    app.logger.info(f"User message: {user_message}")

    start_time = time.perf_counter()  # 開始計時

    try:
        if user_message == '你好':
            reply_message = '你好，有甚麼地方可以為您服務呢?'
        elif user_message == '再見':
            reply_message = '再見，祝您有個美好的一天！'
        else:
            bot_response = chatbot.get_response(user_message)
            reply_message = str(bot_response)

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_message)
        )
    except Exception as e:
        app.logger.error(f"Error handling message: {e}")
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="對不起，我遇到了一些問題，請稍後再試。")
        )
    finally:
        end_time = time.perf_counter()  # 結束計時
        execution_time = end_time - start_time
        app.logger.info(f"Execution time: {execution_time:.4f} seconds")

if __name__ == "__main__":
    app.run()
