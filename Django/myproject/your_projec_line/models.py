# -*- coding: utf-8 -*-
from django.db import models
import sys

# ��l�����j�`�׭���
original_recursion_limit = sys.getrecursionlimit()

# �W�[���j�`�׭���
sys.setrecursionlimit(3000)

class Message(models.Model):
    sender = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.content[:20]}..."

    class Meta:
        app_label = 'your_project_line'

class Statement(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    in_response_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        app_label = 'your_project_line'

# �b�ҫ���󥽧���_��l�����j�`�׭���
sys.setrecursionlimit(original_recursion_limit)
