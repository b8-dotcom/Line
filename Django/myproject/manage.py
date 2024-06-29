#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def main():
    # �]�w Django ���q�{�]�m�Ҷ�
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

    # �W�[���j�`�׭���]�V�ΡA�ھڹ�ڻݨD�վ�^
    original_recursion_limit = sys.getrecursionlimit()  # �����e���j�`�׭���
    sys.setrecursionlimit(3000)  # �]�m�s�����j�`�׭���

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    try:
        # ����R�O����O
        execute_from_command_line(sys.argv)
    finally:
        # ��_��l�����j�`�׭���
        sys.setrecursionlimit(original_recursion_limit)

if __name__ == '__main__':
    main()
