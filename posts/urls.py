from django.urls import path
from . import views as post_views

urlpatterns = [
    path('', post_views.post_view, name="posts"),
    path('like_unlike/', post_views.like_unlike_post, name='like_unlike_post'),
    path('<pk>/delete-post/', post_views.PostDeleteView.as_view(), name="delete_post"),
    path('<pk>/update-post/', post_views.PostUpdateView.as_view(), name="update_post"),
    path('<pk>/delete-comment/', post_views.CommentDeleteView.as_view(), name="delete_comment"),
    path('<pk>/update-comment/', post_views.CommentUpdateView.as_view(), name="update_comment"),
]
