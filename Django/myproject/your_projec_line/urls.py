from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin_panel/', admin.site.urls),  # �N�R�W�Ŷ��q 'admin' �קאּ 'admin_panel'
    path('chatbot/', include('chatterbot_app.urls')),
    # ��L�� URL ���|
]
