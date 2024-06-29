# -*- coding: utf-8 -*-
import os
import django
import collections.abc  # 正確導入 Hashable
from flask import Flask, request, abort
from linebot import LineBotApi
from linebot.v3.webhook import WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import nltk
from nltk.corpus import stopwords, wordnet
import logging
import time
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# 設置 Django 環境變量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_projec_line.settings')  # 替換成你的實際 Django 項目名稱
django.setup()

# LINE 設定
LINE_CHANNEL_ACCESS_TOKEN = '3N+hwqKvNK8MUNVrV4EeboNrD/1liUCyq30MZ241s1BDNKRie2hMywwMBquG72uqVFdQZqL+/TcqsO5sD2De5abt841S4Fb79Y0khqBCIe1jWsVW/JTxlabWkjoYdFfa8zcxOuPhJnjVIb3SJ+fhGwdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_SECRET = '93a8d88c1459c647e0a80e3ea21d95b8'

app = Flask(__name__)
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# 設置日誌
logging.basicConfig(level=logging.INFO)

# 創建 ChatterBot 聊天機器人
chatbot = ChatBot(
    'LearningBot',
    storage_adapter='chatterbot.storage.django_storage.DjangoStorageAdapter',  # 使用 DjangoStorageAdapter
    database_uri='sqlite:///db.sqlite3',  # 替換成您的 Django 數據庫 URI
    read_only=False  # 設置為 False，以便訓練機器人
)

# 訓練 NLTK 語料庫
trainer = ListTrainer(chatbot)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

conversation = [
    "你好",
    "你好,有什麼我可以幫到您的嗎?",
    "再見",
    "再見,祝您有個美好的一天!",
]

trainer.train(conversation)

# 載入 GPT-2 模型
gpt2_model = GPT2LMHeadModel.from_pretrained('gpt2')
gpt2_tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

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
            reply_message = '你好,有什麼我可以幫到您的嗎?'
        elif user_message == '再見':
            reply_message = '再見,祝您有個美好的一天!'
        else:
            # 使用 GPT-2 生成回應
            input_ids = gpt2_tokenizer.encode(user_message, return_tensors='pt')
            output = gpt2_model.generate(input_ids, max_length=50, num_return_sequences=1, do_sample=True, top_k=50, top_p=0.95, num_beams=1)
            reply_message = gpt2_tokenizer.decode(output[0], skip_special_tokens=True)

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_message)
        )
    except LineBotApiError as e:
        app.logger.error(f"Line Bot API error: {e.status_code} {e.error.message}")
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="對不起,我遇到了一些問題,請稍後再試。")
        )
    except Exception as e:
        app.logger.error(f"Error handling message: {e}")
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="對不起,我遇到了一些問題,請稍後再試。")
        )
    finally:
        end_time = time.perf_counter()  # 結束計時
        execution_time = end_time - start_time
        app.logger.info(f"Execution time: {execution_time:.4f} seconds")

if __name__ == "__main__":
    app.run()