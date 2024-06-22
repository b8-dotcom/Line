from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin_panel/', admin.site.urls),  # 將命名空間從 'admin' 修改為 'admin_panel'
    path('chatbot/', include('chatterbot_app.urls')),
    # 其他的 URL 路徑
]
