from django import forms
from .models import *

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title','content']