from django.urls import path
from .views import (
    ProfileListView,
    add_friend,
    remove_friend,
    requests_received,
    accept_request,
    remove_request,
    ProfileDetailView
)

urlpatterns = [
    path('', ProfileListView.as_view(), name='profiles'),
    path('add_friend/', add_friend, name='add_friend'),
    path('remove_friend/', remove_friend, name='remove_friend'),
    path('requests/', requests_received, name='requests'),
    path('accept_request/', accept_request, name="accept_request"),
    path('remove_request/', remove_request, name="remove_request"),
    path('<slug>/', ProfileDetailView.as_view(), name="profile_detail"),
]
