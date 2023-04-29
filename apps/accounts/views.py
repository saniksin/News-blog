from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse
from django.views.generic import FormView, CreateView, TemplateView
from apps.accounts.forms import LoginForm, UserRegisterForm
from .models import User
from django.urls import reverse_lazy
from apps.accounts.utils import send_activation_email
from .token import CustomTokenGenerator

# Create your views here.

class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        email = data["email"]
        password = data["password"]
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect("all")
            else:
                HttpResponse("Ваш аккаунт не активен")
        HttpResponse("Такого пользователя не существует")


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("all")


class UserRegisterView(CreateView):
    model = User
    template_name = "register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("register_done")

    def form_valid(self, form):
        user = form.save()
        send_activation_email(user, request=self.request, to_email=user.email)
        return super().form_valid(form)

class RegisterDoneView(TemplateView):
    template_name = 'register_done.html'


from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator, PasswordResetTokenGenerator
from django.http import Http404

def activate_account(request, uidb64, token):
    try:
        uid = int(force_str(urlsafe_base64_decode(uidb64)))
        user = User.objects.get(pk=uid)
    except (ValueError, User.DoesNotExist, TypeError):
        user = None
    if user is not None and CustomTokenGenerator().check_token(user, token):
        user.is_verified = True
        login(request, user)
        print('Я зашел типо сюда!!!!!!!')
        return redirect(reverse_lazy('all'))
    raise Http404