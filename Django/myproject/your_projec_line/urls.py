# your_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', include('django_orm.urls')),  # 將 'chatterbot_app.urls' 改為 'django_orm.urls'
    # 其他的 URL 路徑配置
]
