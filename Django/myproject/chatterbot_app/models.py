from django.db import models

# Create your models here.

# 在 chatterbot_app/models.py 文件中定義模型
from django.db import models

class Message(models.Model):
    user_id = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

