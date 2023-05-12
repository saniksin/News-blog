from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from apps.api.serializers import PostSerializer, CategorySerializer
from apps.blog.models import Post, Category

# Create your views here.
class PostListApiView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_active=True)
    permission_classes = [IsAuthenticated]


class CategoryListApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]