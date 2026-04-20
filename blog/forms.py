from .models import Blog, Photo
from django import forms

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'caption']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']