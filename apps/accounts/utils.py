from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.utils.encoding import force_bytes  
from django.core.mail import EmailMessage 
from apps.accounts.models import User
from .token import CustomTokenGenerator

def send_activation_email(user, request, to_email):
    email_subject = "Подтверждение аккаунта на сайта newsblog.com"
    protocol = 'https' if request.is_secure() else 'http'
    
    data = {
        "protocol": protocol,
        "domain": get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': CustomTokenGenerator().make_token(user),
        'user': user
    }
    
    check = CustomTokenGenerator().check_token(user, data['token'])
    print(check)

    print("User:", user)
    print("Token:", data['token'])
    print("User in send_activation_email:", user.pk)




    

    message = render_to_string("register_confirm_email.html",data)
    email = EmailMessage(email_subject, message, to=[to_email])
    email.content_subtype = "html"
    email.send(fail_silently=True)