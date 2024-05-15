from django.urls import path, re_path

from module.chat.views import new_friend
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

urlpatterns = [
    path("new-friend/", new_friend, name="new friend"),
]

