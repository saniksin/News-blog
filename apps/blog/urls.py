from django.urls import path

from apps.blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name="all"),
    path('post/<int:pk>/', views.PostDelailView.as_view(), name="post_detail"),
    path('post/list/<str:slug>/', views.PostListView.as_view(), name='post_list')
]

