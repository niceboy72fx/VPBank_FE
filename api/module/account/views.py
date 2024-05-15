import re
from util.authen import NoAuthentication
from module.account.models import OneTimePassword, User
from util.otp import send_code_to_user
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView
from .serializers import  AccountSerializer, LogoutSerializer, PasswordResetRequestSerializer, UserLoginSerializer, UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets

from module.account import serializers
from module.account.filter import UserFilter

class RegisterUserView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    authentication_classes = [NoAuthentication]
    permission_classes = [AllowAny]
    
    
    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)
        if serializer.is_valid():
            serializer.save()
            user = serializer.data
            send_code_to_user(user_data['email'])
            return Response(
                {
                    'data':user,
                    'messager': f'OK'
                }
            , status = status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
class VerifyUserEmail(GenericAPIView):
    authentication_classes = [NoAuthentication]
    permission_classes = [AllowAny]
    
    def post(self, request):
        otp_code = request.data['otp_code']
        try:
            user_code_obj = OneTimePassword.objects.get(code=otp_code)
            user = user_code_obj.user
            if not user.is_active:
                user.is_active = True
                user.save()
                return Response({
                    'message': 'account and mail are verified successfully!',
                }, status = status.HTTP_200_OK)
            return Response({
                    'message': 'code is invalid user has been verified !',
                }, status = status.HTTP_200_OK)
        except OneTimePassword.DoesNotExist:
            return Response({'message': 'passcode is not matching'}, status = status.HTTP_400_BAD_REQUEST)



class LoginUserView(GenericAPIView):
    serializer_class = UserLoginSerializer
    authentication_classes = [NoAuthentication]
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class PasswordResetRequestView(GenericAPIView):
#     pass

class PasswordResetConfirm(GenericAPIView):
     serializers_class = PasswordResetRequestSerializer
     authentication_classes = [NoAuthentication]
     permission_classes = [AllowAny]
     
     def post(self, request):
         serializers = self.serializers_class(data = request_data, context={'request': request})
         serializers.is_valid(raise_exception = True)
         return Response({'message':'we have sent you a link to reset your password'}, status=status.HTTP_200_OK)
     
# class SetNewPasswordView(GenericAPIView):
#     pass

class LogoutApiView(GenericAPIView):
    serializers_class = LogoutSerializer
    authentication_classes = [NoAuthentication]
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = self.serializers_class(data =  request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
   
class AccountView(mixins.RetrieveModelMixin ,mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializers_class = AccountSerializer
    search_fields = ("first_name", "last_name", "email", "phone_number")
    filterset_class = UserFilter
    queryset = User.objects.all()
    authentication_classes = [NoAuthentication]
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        queryset = self.queryset
        queryset = self.filter_queryset(queryset)
        return queryset
    
    
    # def post(self, request):
    #     pass
    
    # def infor_account(self, request):
    #     pass
    
    # @action(method = "GET")
    def list(self, request, *arg, **kwargs):
        return self.list(request, *arg, **kwargs)
