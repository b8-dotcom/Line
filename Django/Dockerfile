# 使用官方 Python 映像作為基礎映像
FROM python:3.11.9

# 設置工作目錄
WORKDIR /app

# 複製項目的依賴文件到容器中
COPY requirements.txt /app/requirements.txt

# 安裝依賴
RUN pip install --no-cache-dir -r requirements.txt

# 複製項目文件到容器中
COPY line /app/linebot


# 指定容器啟動時運行的命令
CMD ["python", "app.py"]
