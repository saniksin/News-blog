from django import forms
from apps.blog.models import Comment, Post

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text":forms.Textarea(attrs={"class":"form-control"})
        }


class PostCreationForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            "title", 
            "image",
            "description",
            "category",
            "is_active",
        ]

        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
            "description": forms.Textarea(attrs={"class":"form-control"}),
            "category": forms.Select(attrs={"class":"form-control"}),
            #'is_active': forms.CheckboxInput(attrs={"class":"form-control"})
        }
        
