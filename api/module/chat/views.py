from module.chat.serializers import NewFriendSerializer
from rest_framework.response import Response
from rest_framework import status

from module.chat.models import Friend, RoomChat, UserRoom
from module.account.models import User

# Create your views here.

def new_friend(request):
    if request.method == 'POST':
        serializer = NewFriendSerializer(data=request.data)
        serializer.is_valid(raise_exceptions=True)
        return Response({"message":"added new friend successfully !"}, status=status.HTTP_200_BAD_REQUEST)

