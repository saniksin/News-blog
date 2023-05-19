from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView, 
    CreateAPIView
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.serializers import *
from apps.blog.models import Post, Category
from django.shortcuts import get_object_or_404

# Create your views here.
class PostListApiView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_active=True)
    permission_classes = [IsAuthenticated]


class CategoryListApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]


class PostDetailAPIView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_active=True)
    permission_classes = [IsAuthenticated]


class LikePostAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            return Response(
                {"status": "OK", 
                 "details": "Your like removed"})
        else:
            post.likes.add(request.user)
            return Response(
                {"status": "OK", 
                 "details": "Your liked post"})
        

class PostCreateAPIView(CreateAPIView):
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)
    

class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategoryCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return super().perform_create(serializer)
    

class UsersAPIView(ListAPIView):
    serializer_class = UsersSerializer
    queryset = User.objects.values('id', 'email')
    permission_classes = [IsAdminUser]



class UsersDetailAPIView(RetrieveAPIView):
    serializer_class = UsersDetailSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    