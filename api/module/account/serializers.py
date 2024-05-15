from util.otp import send_normal_email
from .models import User
from rest_framework import serializers
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import smart_str, force_str, smart_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=6, write_only=True)
    re_password = serializers.CharField(max_length=255, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'password', 're_password']
    
    def validate(self, data):
        password = data.get('password', '')
        re_password = data.get('re_password', '')
        if password != re_password:
            raise serializers.ValidationError("Passwords do not match!")
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['first_name'] + ' ' + validated_data['last_name'],
            phone_number=validated_data.get('phone_number', ''),  # Optional field
            password=validated_data['password'],
            is_active = False
        )
        return user
    


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=155, min_length=6)
    password=serializers.CharField(max_length=68, write_only=True)
    username=serializers.CharField(max_length=255, read_only=True)
    access_token=serializers.CharField(max_length=255, read_only=True)
    refresh_token=serializers.CharField(max_length=255, read_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'password',  'username', 'access_token', 'refresh_token']
        
    def validate(self, attr):
        email = attr.get('email')
        password = attr.get('password')
        request = self.context.get('request')
        find_user = User.objects.filter(email=email).first()
        user = authenticate(request, username=find_user.username, password=password)
        if not user:
            raise AuthenticationFailed("invalid credentials !")
        if not user.is_active:
            raise AuthenticationFailed("Email is not verified")
        token = user.tokens()
        
        return {
            'email': email,
            'username': user.username,
            "access_token":str(token.get('access')),
            "refresh_token":str(token.get('refresh'))
        }
        
class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    
    class Meta:
        field = ['email']
        
    def validate(self, request):
        email =request.get('email')
        if User.objects.get(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user) ## using to generate token path 
            request = self.context.get('request')
            current_site = get_current_site(request).domain
            relative_link =reverse('reset-password-confirm', kwargs={'uidb64':uidb64, 'token':token})
            abslink=f"http://{current_site}{relative_link}"
            email_body=f"Hi {user.first_name} use the link below to reset your password {abslink}"
            data={
                'email_body':email_body, 
                'email_subject':"Reset your Password", 
                'to_email':user.email
                }
            send_normal_email(data)

        return super().validate(request)
    
    
            
class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
    
    class Meta:
        field = ['refresh_token']
        
        
    def validate(self, request):
        self.token  = request.get('refresh_token')
        return request
    
    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except TokenError:
            return {"error": "Token is expired or invalid"}
            
class AccountSerializer(serializers.Serializer):
    
    class Meta:
        model = User
        field = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "phone_number",
            "gender",
            "role",
        )
        
class UserSearchingSerializer(serializers.Serializer):
    class Meta:
        models = User
        fields = ("first_name", "last_name", "username", "email", "phone_number")