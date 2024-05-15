from django.utils import timezone
import random
from module.account.models import OneTimePassword, User
from django.core.mail import EmailMessage, get_connection
from django.conf import settings

def generateOtp():
    otp = ""
    for i in range(6):
        otp += str(random.randint(1,9))
    return otp

def send_code_to_user(email):
    Subject = "One time to verify your email address !"
    otp_code = generateOtp()
    user = User.objects.get(email=email)
    current_site = "My VinMec "
    email_body = f"Hi {user.first_name} thanks for siging up on {current_site}, Here's your OTP {otp_code} code to verify your email address"
    OneTimePassword.objects.create(user = user, code = otp_code , timestamp=timezone.now() , expired_at=timezone.now()) 
    connection =  get_connection(  
            host=settings.EMAIL_HOST, 
            port=settings.EMAIL_PORT,  
            username=settings.EMAIL_HOST_USER, 
            password=settings.EMAIL_HOST_PASSWORD, 
            use_tls=settings.EMAIL_USE_TLS  
    )
    subject = Subject
    email_from = settings.DEFAULT_FROM_EMAIL 
    recipient_list = [email]  
    message = email_body  
    email_message = EmailMessage(subject, message, email_from, recipient_list, connection=connection)
    email_message.send()
    connection.close()
    
def send_normal_email(data):
    email=EmailMessage(
        subject=data['email_subject'],
        body=data['email_body'],
        from_email=settings.EMAIL_HOST_USER,
        to=[data['to_email']]
    )
    email.send()