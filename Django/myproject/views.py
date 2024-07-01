# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging

logger = logging.getLogger(__name__)

class ChatBotView(View):
    chatbot = ChatBot(
        'Example Bot',
        database_uri='sqlite:///db.sqlite3'
    )
    
    # 初始训练（可选）
    trainer = ListTrainer(chatbot)
    trainer.train([
        "Hi, can I help you?",
        "Sure, I'd like to book a flight to Iceland.",
        "Your flight has been booked."
    ])

    def get(self, request):
        user_message = request.GET.get('message')
        if user_message:
            logger.debug(f"User message: {user_message}")
            response = self.chatbot.get_response(user_message)
            logger.debug(f"Bot response: {response}")
            return JsonResponse({'response': str(response)})
        else:
            return JsonResponse({'error': 'No message provided'}, status=400)
