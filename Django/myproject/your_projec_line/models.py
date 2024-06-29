# -*- coding: utf-8 -*-
from django.db import models
import sys

# 原始的遞迴深度限制
original_recursion_limit = sys.getrecursionlimit()

# 增加遞迴深度限制
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

# 在模型文件末尾恢復原始的遞迴深度限制
sys.setrecursionlimit(original_recursion_limit)
