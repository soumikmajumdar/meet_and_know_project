from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'type here', 'class':'post-text-box'}))
    class Meta:
        model = Post
        fields = ['content', 'image']

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'type here', 'class':'post-text-box'}))
    class Meta:
        model = Post
        fields = ['content']
