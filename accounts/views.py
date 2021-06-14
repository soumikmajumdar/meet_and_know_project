from django.shortcuts import render, redirect
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
        user = self.request.user
        me = Profile.objects.get(user=user)
        rel_r = Relationship.objects.filter(sender=me)
        rel_s = Relationship.objects.filter(receiver=me)
        rel_receiver = [rel.receiver.user for rel in rel_r]
        rel_sender = [rel.sender.user for rel in rel_r]
        context['rel_receiver'] = rel_receiver
        context['rel_sender'] = rel_sender
        return context

def add_friend(request):
    if request.method == "POST":
        sender = Profile.objects.get(user=request.user)
        receiver = Profile.objects.get(pk=request.POST.get('profile_pk'))
        relationship = Relationship.objects.create(sender=sender, receiver=receiver, status='sent')

        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profiles')
