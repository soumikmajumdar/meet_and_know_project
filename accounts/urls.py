from django.urls import path
from .views import (
    ProfileListView,
    add_friend,
)

urlpatterns = [
    path('', ProfileListView.as_view(), name='profiles'),
    path('add_friend/', add_friend, name='add_friend'),
]
