from django.shortcuts import render
from .models import Profile, Relationship
from django.views.generic import ListView

class ProfileListView(ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = 'accounts/profiles.html'

    def get_queryset(self):
        profiles = Profile.objects.other_profiles(self.request.user)
        return profiles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        to_friend = Profile.objects.to_friend(self.request.user)
        context['to_friend'] = to_friend
        return context

def friends(request):
    to_friend = Profile.objects.to_friend(request.user)

    return render(request, 'accounts/friend.html', {'to_friend':to_friend})
