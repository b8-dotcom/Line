# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 14:33:14 2024

@author: 88693
"""

pip install flask   
pip install line-bot-sdk
pip install chatterbot
pip install chatterbot_corpus

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# LINE 設定
LINE_CHANNEL_ACCESS_TOKEN = '3N+hwqKvNK8MUNVrV4EeboNrD/1liUCyq30MZ241s1BDNKRie2hMywwMBquG72uqVFdQZqL+/TcqsO5sD2De5abt841S4Fb79Y0khqBCIe1jWsVW/JTxlabWkjoYdFfa8zcxOuPhJnjVIb3SJ+fhGwdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_SECRET = '93a8d88c1459c647e0a80e3ea21d95b8'

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# 建立 ChatterBot 聊天機器人
chatbot = ChatBot('LearningBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
<<<<<<< HEAD
    
    if user_message == '你好':
=======

if user_message == '你好':
>>>>>>> 37ede5d72b9263a4ac305317fd769225e71e40c8
        reply_message = '你好！'
    elif user_message == '再見':
        reply_message = '再見，祝你有個美好的一天！'
    else:
        reply_message = '我不太明白你的意思。'

    bot_response = chatbot.get_response(user_message)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=str(bot_response))
    )

if __name__ == "__main__":
    app.run()





