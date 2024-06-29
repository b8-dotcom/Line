# 進入 Django shell
python manage.py shell

# 導入必要的模型
from your_project_name.models import Conversation

# 創建一個新的對話
conversation = Conversation(user_id='user123', message='Hello!')
conversation.save()

# 查詢所有對話
all_conversations = Conversation.objects.all()
for conv in all_conversations:
    print(conv.user_id, conv.message)

# 根據條件查詢對話
user123_conversations = Conversation.objects.filter(user_id='user123')
for conv in user123_conversations:
    print(conv.user_id, conv.message)

# 更新對話
conv_to_update = Conversation.objects.get(id=1)
conv_to_update.message = 'Updated message'
conv_to_update.save()

# 刪除對話
conv_to_delete = Conversation.objects.get(id=2)
conv_to_delete.delete()

# 退出 Django shell
exit()
