from django.urls import path
from .views import ChatBotView  # �T�O views.py ���� ChatBotView ���w�q

urlpatterns = [
    path('', ChatBotView.as_view(), name='home'),
    # �i�H�K�[��h���|�t�m
]
