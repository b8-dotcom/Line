# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:29:41 2024

@author: 88693
"""

import json

# 讀取 Pipfile.lock 文件
with open('Pipfile.lock') as f:
    pipfile_lock = json.load(f)

# 打開 requirements.txt 文件準備寫入
with open('requirements.txt', 'w') as f:
    # 處理 default 部分
    for package, details in pipfile_lock.get('default', {}).items():
        f.write(f"{package}{details['version']}\n")
    
    # 處理 develop 部分
    for package, details in pipfile_lock.get('develop', {}).items():
        f.write(f"{package}{details['version']}\n")

print("requirements.txt 生成成功！")
