from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

def get_user_id_from_token(request):
        authorization_header = request.headers.get('Authorization')
        try:
            token = authorization_header.split(' ')[1]
            decoded_token = RefreshToken(token)
            user_id = decoded_token.payload['user_id']
            return user_id
        except Exception as e:
            print('Error decoding token')
