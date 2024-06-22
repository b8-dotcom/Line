from django.conf import settings
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from collections import Hashable  # 導入 Hashable

# 初始化 ChatBot
chatbot_settings = settings.CHATTERBOT.copy()
logic_adapters = chatbot_settings.pop('logic_adapters', [])

chatbot_settings.update({
    'logic_adapters': logic_adapters,
})

chatbot = ChatBot(**chatbot_settings)

# 選擇性地訓練機器人
trainer = ListTrainer(chatbot)
for conversation in chatbot_settings.get('對話庫', []):
    trainer.train(conversation)

class YourView(View):
    def get(self, request):
        return render(request, 'your_template.html')

def get_response(request):
    user_message = request.GET.get('message')
    response = chatbot.get_response(user_message)
    return JsonResponse({'response': str(response)})

# 確保在使用 Hashable 的地方正確引用
# 修改程式碼中使用 collections.Hashable 的部分
# 示例：假設在某個地方使用了 collections.Hashable
# 修改為使用 collections.abc.Hashable
# if not isinstance(key, collections.Hashable):
#     # 做一些處理
# 修改為
# if not isinstance(key, Hashable):
#     # 做一些處理
