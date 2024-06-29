#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def main():
    # 設定 Django 的默認設置模塊
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

    # 增加遞迴深度限制（慎用，根據實際需求調整）
    original_recursion_limit = sys.getrecursionlimit()  # 獲取當前遞迴深度限制
    sys.setrecursionlimit(3000)  # 設置新的遞迴深度限制

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    try:
        # 執行命令行指令
        execute_from_command_line(sys.argv)
    finally:
        # 恢復原始的遞迴深度限制
        sys.setrecursionlimit(original_recursion_limit)

if __name__ == '__main__':
    main()
