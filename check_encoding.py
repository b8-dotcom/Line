file_path = 'Pipfile'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    print("文件使用 UTF-8 編碼，且沒有發現問題。")
except UnicodeDecodeError as e:
    print(f"文件包含非 UTF-8 編碼的字符: {e}")
