from django.shortcuts import render
from .forms import PostForm, CommentForm
from accounts.models import Profile
from .models import Post

def post_view(request):
    author = Profile.objects.get(user=request.user)
    posts = Post.objects.all()
    p_form = PostForm()
    c_form = CommentForm()

    if 'submit_p_form' in request.POST:
        p_form = PostForm(request.POST, request.FILES)
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            instance.author = author
            instance.save()
            p_form= PostForm()



    context = {
        'posts'     : posts,
        'p_form'    : p_form,
        'c_form'    : c_form
    }

    return render(request, 'posts/post_view.html', context)
