from django import forms
from firstapp.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = "__all__"
