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
        user = self.request.user
        me = Profile.objects.get(user=user)
        rel_r = Relationship.objects.filter(sender=me)
        rel_s = Relationship.objects.filter(receiver=me)
        rel_receiver = [rel.receiver.user for rel in rel_r]
        rel_sender = [rel.sender.user for rel in rel_r]
        context['to_friend'] = to_friend
        context['rel_receiver'] = rel_receiver
        context['rel_sender'] = rel_sender
        context['user'] = user
        return context
