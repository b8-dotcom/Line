import os

# 語料庫路徑，根據您的安裝位置進行調整
corpus_path = r'C:\Users\88693\AppData\Local\Programs\Python\Python312\Lib\site-packages\chatterbot_corpus\data'

# 列出所有文件
def list_files():
    for root, dirs, files in os.walk(corpus_path):
        for file in files:
            print(os.path.join(root, file))

if __name__ == "__main__":
    list_files()
