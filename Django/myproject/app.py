from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import torch.nn as nn
from .models import Statement

# 初始化 GPT-2
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# 初始化 LSTM 模型
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

class ChatBotView(View):
    def get(self, request):
        return render(request, 'home.html')  # 替換為你的模板

    def post(self, request):
        user_message = request.POST.get('message')
        
        # 使用 ORM 查詢來進行對話
        try:
            statement = Statement.objects.get(text=user_message)
            orm_response = statement.text  # 假設你從 ORM 中取得回應的文本
        except Statement.DoesNotExist:
            orm_response = "抱歉，我不明白您的問題。"

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
            'orm_response': orm_response,
            'gpt2_response': gpt2_response,
            'lstm_response': lstm_response
        })
