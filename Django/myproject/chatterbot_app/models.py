# chatterbot_app/models.py

from django.db import models

class Message(models.Model):
    user_id = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        app_label = 'chatterbot_app'
