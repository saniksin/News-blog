from typing import Any, Dict
from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from apps.blog.models import Post, Category, Comment
from apps.blog.forms import CommentForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context

from django.shortcuts import redirect
from django.urls import reverse_lazy

def save_comment_form(request, post_id):
    if request.method == "POST":
        print(request.POST)
        form = CommentForm(request.POST)
        if form.is_valid():
            post = get_object_or_404(Post, id=post_id)
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
    return redirect(reverse_lazy("post_detail", kwargs={"pk":post_id}))