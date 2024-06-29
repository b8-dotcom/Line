from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import torch.nn as nn

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

# 初始化 LSTM 模型
vocab_size = len(tokenizer)
embedding_dim = 128
hidden_dim = 256
lstm_model = LSTMModel(vocab_size, embedding_dim, hidden_dim)

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
        
        # 使用 LSTM 模型生成回應
        hidden = lstm_model.init_hidden()
        for i in range(len(user_message.split())):
            token = tokenizer.encode(user_message.split()[i], return_tensors='pt')
            output, hidden = lstm_model(token, hidden)
        lstm_response = tokenizer.decode(output.argmax(dim=1), skip_special_tokens=True)
        
        return JsonResponse({
            'chatterbot_response': str(chatterbot_response),
            'gpt2_response': gpt2_response,
            'lstm_response': lstm_response
        })

class LSTMModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim):
        super(LSTMModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim, vocab_size)

    def forward(self, input, hidden):
        embedded = self.embedding(input).view(1, 1, -1)
        output, hidden = self.lstm(embedded, hidden)
        output = self.fc(output[0])
        return output, hidden

    def init_hidden(self):
        return (torch.zeros(1, 1, self.hidden_dim),
                torch.zeros(1, 1, self.hidden_dim))