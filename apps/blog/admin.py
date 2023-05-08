from django.contrib import admin
from django.forms import ModelForm, CharField

# Register your models here.
from apps.blog.models import Post, Category
from ckeditor.widgets import CKEditorWidget

class PostAdminForm(ModelForm):
    description = CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = "__all__"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = [
        "title", "author", "created_at", "updated_at", "is_active"
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name", "slug", "id"
    ]

    prepopulated_fields = {"slug":("name", )}