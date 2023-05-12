from django.urls import path
from apps.api import views

urlpatterns = [
    path('posts/', views.PostListApiView.as_view()),
    path('category/', views.CategoryListApiView.as_view()),
]