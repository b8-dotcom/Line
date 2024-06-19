# -*- coding: utf-8 -*-
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.exceptions import InvalidSignatureError
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

app = Flask(__name__)

# LINE 設定
LINE_CHANNEL_ACCESS_TOKEN = 'YOUR_CHANNEL_ACCESS_TOKEN'
LINE_CHANNEL_SECRET = 'YOUR_CHANNEL_SECRET'

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# 設定日誌
logging.basicConfig(level=logging.INFO)

# 建立 ChatterBot 聊天機器人
chatbot = ChatBot('LearningBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

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

    try:
        if user_message == '你好':
            reply_message = '你好！'
        elif user_message == '再見':
            reply_message = '再見，祝你有個美好的一天！'
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

if __name__ == "__main__":
    app.run()
