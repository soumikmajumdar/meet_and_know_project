from django.urls import path
from .views import ProfileListView, friends


urlpatterns = [
    path('', ProfileListView.as_view(), name='profiles'),
    path('f/', friends)
]
