import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer

from module.account.models import User
from .models import ChatMessage,  RoomChat, UserRoom


class ChatConsumer(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        self.chat_room = self.scope['url_route']['kwargs']['room_id']
        try:
            if RoomChat.object.filter(id=self.chat_room).exists():
                self.channel_layer.group_add(
                    self.chat_room,
                    self.channel_name
                )
                await self.accept()
        except Exception as e:
                await self.close()
        

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.chat_room,
            self.channel_name
        )
        await self.close()

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        user_id = data['user_id']
        room_chat = data['room_chat']
        await self.save_message(user_id, room_chat, message)
        await self.channel_layer.group_send(
            self.chat_room,
            {
                'type': 'chat_message',
                'message': message,
                'user_id': user_id
            }
        )


    async def save_message(self, user_id, room_chat, message):
        user = User.objects.get(id=user_id)
        room_chat = RoomChat.objects.get(id=room_chat)
        chat_message = ChatMessage.objects.create(
            user=user,
            message=message
        )
        room_chat.chat_messages.add(chat_message)
        
    
        
        
    