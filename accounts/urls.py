from django.urls import path
from .views import trial

urlpatterns = [
    path('', trial)
]
