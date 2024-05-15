import uuid

from django.db import models
from module.account.models import User




class ChatMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.CharField(max_length=10000)
    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats')
    
    class Meta:
        ordering = ['date']
        verbose_name_plural = "Messages"


class RoomChat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class UserRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms')
    room = models.ForeignKey(RoomChat, on_delete=models.CASCADE, related_name='members')


class Friend(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')

