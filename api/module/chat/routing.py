from module.chat.consumers import ChatConsumer
from django.urls import path, include, re_path


urlpattern = [
        path('<room_id>/', ChatConsumer.as_asgi()),
]