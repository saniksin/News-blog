from django.urls import path
from apps.accounts import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.user_logout, name="logout"),

    #for registation
    path("register/done", views.RegisterDoneView.as_view(), name="register_done"),
    path("register/", views.UserRegisterView.as_view(), name="register"),

    #url for usr activation
    path("register/confirm/<uidb64>/<token>/", views.activate_account, name="activate_account")
]