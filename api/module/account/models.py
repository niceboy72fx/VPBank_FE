import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from module.account.manager.userManager import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from enum import Enum

class Role(Enum):
    ADMIN = 'Admin'
    USER = 'User'
    STAFF = 'Staff'
    


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = PhoneNumberField(unique=True, null= True, blank=True)
    refresh_token_signature = models.CharField(max_length=128, blank= True, default = True)
    gender = models.CharField(max_length=128, blank= True)
    bio = models.CharField(max_length=255, blank= True)
    role = models.CharField(max_length=50, choices=[(role.value, role.value) for role in Role], default=Role.USER.value)    
    
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = UserManager()
    
    @property
    def full_name(self):
        return f'{self.last_name} + {self.first_name}'
    
    
    def tokens(self):    
        refresh = RefreshToken.for_user(self)
        return {
            "refresh":str(refresh),
            "access":str(refresh.access_token)
        }

    
class OneTimePassword(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    code = models.CharField(max_length=6, unique = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField(auto_now_add=True)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    bio = models.CharField(max_length=100)
    # image = models.ImageField(upload_to="user_images", default="default.jpg")

    def save(self, *args, **kwargs):
        self.full_name = self.user.username
        super(Profile, self).save(*args, **kwargs)