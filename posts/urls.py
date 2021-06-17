from django.urls import path
from . import views as post_views

urlpatterns = [
    path('', post_views.post_view, name="posts"),
    path('like_unlike/', post_views.like_unlike_post, name='like_unlike_post'),
    path('<pk>/delete/', post_views.PostDeleteView.as_view(), name="delete"),
    path('<pk>/update/', post_views.PostUpdateView.as_view(), name="update"),    
]
