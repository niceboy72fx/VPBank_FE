from django.urls import path, include, re_path
from channels.routing import  URLRouter
from module.chat.routing import urlpattern

websocket_urlpatterns = [
    path('ws/api/v1/chat', URLRouter(urlpattern)),
]