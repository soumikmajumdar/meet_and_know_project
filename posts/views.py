from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from accounts.models import Profile
from .models import Post, Like, Comment

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


    if 'submit_c_form' in request.POST:
        c_form  = CommentForm(request.POST)
        post = Post.objects.get(pk=request.POST.get('post_pk'))
        if c_form .is_valid():
            instance = c_form.save(commit=False)
            instance.author = author
            instance.post = post
            instance.save()
            c_form = CommentForm()



    context = {
        'author'    : author,
        'posts'     : posts,
        'p_form'    : p_form,
        'c_form'    : c_form
    }

    return render(request, 'posts/post_view.html', context)


def like_unlike_post(request):
    if request.method == 'POST':
        post = Post.objects.get(pk=request.POST.get('post_pk'))
        user = Profile.objects.get(user=request.user)
        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)

        like, created = Like.objects.get_or_create(user=user, post=post)

        if  not created:
            if like.status == "like":
                like.status = "unlike"
            else:
                like.status = "like"
        else:
            like.status = "like"
        post.save()
        like.save()

    return redirect('posts')
