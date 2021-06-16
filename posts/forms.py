from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'type here', 'class':'post-text-box'}))
    # image = forms.ImageField(label="",widget=forms.(attrs={'class':'image-btn'}))
    class Meta:
        model = Post
        fields = ['content', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
