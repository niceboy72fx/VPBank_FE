from util.parseToken import get_user_id_from_token
from rest_framework import serializers

from module.account.models import User
from module.chat.models import Friend, RoomChat, UserRoom


class NewFriendSerializer(serializers.Serializer):
    friend_id = serializers.CharField(max_length=255)
    
    class Meta:
        model = Friend 
        field = ['friend_id']
        
    def validate(self, request):
        friend_id =request.get('friend_id')
        if not User.objects.get(pk=friend_id).exists():
            raise serializers.ValidationError("Invalid friend_id")
        friend = User.objects.filter(id=friend_id).first()
        user_id = get_user_id_from_token(request)
        user = User.objects.filter(id=user_id).first()
        friend = Friend.objects.create(user=user, friend=friend)
        room = RoomChat.objects.create()
        UserRoom.objects.create(user=user, room=room)
        UserRoom.objects.create(user=friend, room=room)
        return request