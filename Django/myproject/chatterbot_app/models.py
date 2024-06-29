# 在 your_app/models.py 文件中定義模型
from django.db import models

class Message(models.Model):
    user_id = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
