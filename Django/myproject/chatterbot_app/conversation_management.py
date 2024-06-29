# �i�J Django shell
python manage.py shell

# �ɤJ���n���ҫ�
from your_project_name.models import Conversation

# �Ыؤ@�ӷs�����
conversation = Conversation(user_id='user123', message='Hello!')
conversation.save()

# �d�ߩҦ����
all_conversations = Conversation.objects.all()
for conv in all_conversations:
    print(conv.user_id, conv.message)

# �ھڱ���d�߹��
user123_conversations = Conversation.objects.filter(user_id='user123')
for conv in user123_conversations:
    print(conv.user_id, conv.message)

# ��s���
conv_to_update = Conversation.objects.get(id=1)
conv_to_update.message = 'Updated message'
conv_to_update.save()

# �R�����
conv_to_delete = Conversation.objects.get(id=2)
conv_to_delete.delete()

# �h�X Django shell
exit()
