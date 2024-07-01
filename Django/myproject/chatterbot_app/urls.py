from django.urls import path
from .views import ChatBotView  # 確保 views.py 中有 ChatBotView 的定義

urlpatterns = [
    path('', ChatBotView.as_view(), name='home'),
    # 可以添加更多路徑配置
]
