# views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Initialize ChatBot
chatbot = ChatBot(**settings.CHATTERBOT)

# Optionally, train the bot
trainer = ListTrainer(chatbot)
trainer.train(settings.CHATTERBOT['training_data'])

class YourView(View):
    def get(self, request):
        return render(request, 'your_template.html')  # 替換為你的模板

def get_response(request):
    user_message = request.GET.get('message')
    response = chatbot.get_response(user_message)
    return JsonResponse({'response': str(response)})
