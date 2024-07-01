# myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatterbot_app.urls')),  # 將您的應用程序的路徑包含在內
]
