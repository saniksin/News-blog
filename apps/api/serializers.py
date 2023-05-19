from rest_framework import serializers
from apps.blog.models import Post, Category
from apps.accounts.models import User


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            "title",
            "description",
            "category",
            "image",
        ]


class CategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            "name",
            "slug",
        ]


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'email',
        ]


class UsersDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"