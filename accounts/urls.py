from django.urls import path
from .views import ProfileListView


urlpatterns = [
    path('', ProfileListView.as_view(), name='profiles'),
]
