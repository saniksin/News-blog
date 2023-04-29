from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from apps.blog.models import Post, Category

# Create your views here.

# ListView - Это базовый generic класс с помощью которого можно выводить список записей

class PostListView(ListView):
    template_name = 'index.html'
    model = Post
    queryset = Post.objects.filter(is_active=True)
    context_object_name = "posts"
    paginate_by = 2

    def get_queryset(self):
        category_slug = self.kwargs.get("slug")
        if category_slug:
            return Post.objects.filter(category__slug=category_slug)
        else:
            return Post.objects.all()

class PostDelailView(DetailView):
    template_name = "post_detail.html"
    model = Post
    queryset = Post.objects.filter(is_active=True)
    context_object_name = "post"