# your_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', include('chatterbot_app.urls')),
    # ��L�� URL ���|�t�m
]
