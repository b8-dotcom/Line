# your_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', include('django_orm.urls')),  # �N 'chatterbot_app.urls' �אּ 'django_orm.urls'
    # ��L�� URL ���|�t�m
]
