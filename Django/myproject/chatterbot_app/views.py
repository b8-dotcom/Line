from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# 初始化 ChatBot
chatbot = ChatBot(
    name=settings.CHATTERBOT['name']['en'],
    logic_adapters=settings.CHATTERBOT['logic_adapters']
)

# 使用 ChatterBotCorpusTrainer 訓練機器人
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.greetings", "chatterbot.corpus.english.conversations")

# 初始化 GPT-2
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# 下載 NLTK 所需資源
nltk.download('stopwords')
nltk.download('punkt')

class ChatBotView(View):
    def get(self, request):
        return render(request, 'home.html')  # 替換為你的模板

    def post(self, request):
        user_message = request.POST.get('message')
        
        # 使用 ChatterBot 進行對話
        chatterbot_response = chatbot.get_response(user_message)
        
        # 使用 GPT-2 進行對話
        inputs = tokenizer.encode(user_message, return_tensors='pt')
        outputs = model.generate(inputs, max_length=100, num_return_sequences=1, do_sample=True, top_k=50, top_p=0.95, num_iterations=1, no_repeat_ngram_size=2, bad_words_ids=[[14098, 30086, 30087, 30088]])
        gpt2_response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # 過濾 GPT-2 生成的文本
        stop_words = set(stopwords.words('english'))
        filtered_gpt2_response = ' '.join([word for word in gpt2_response.split() if word.lower() not in stop_words])
        
        return JsonResponse({
            'chatterbot_response': str(chatterbot_response),
            'gpt2_response': filtered_gpt2_response
        })