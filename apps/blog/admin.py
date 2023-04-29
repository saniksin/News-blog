from django.contrib import admin

# Register your models here.
from apps.blog.models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title", "author", "created_at", "updated_at", "is_active"
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name", "slug", "id"
    ]