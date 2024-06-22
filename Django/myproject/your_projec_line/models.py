from django.db import models


class Message(models.Model):
    sender = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.content[:20]}..."

    class Meta:
        app_label = 'your_projec_line'

class Statement(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    in_response_to = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        app_label = 'your_projec_line'
