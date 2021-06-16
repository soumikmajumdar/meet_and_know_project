from django.shortcuts import render
from .forms import PostForm, CommentForm
from accounts.models import Profile
from .models import Post

def post_view(request):
    posts = Post.objects.all()
    p_form = PostForm()
    c_form = CommentForm()


    context = {
        'posts'     : posts,
        'p_form'    : p_form,
        'c_form'    : c_form
    }

    return render(request, 'posts/post_view.html', context)
