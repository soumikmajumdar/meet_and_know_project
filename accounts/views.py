from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Relationship
from django.views.generic import ListView, DetailView
from django.db.models import Q

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

def remove_friend(request):
    if request.method == "POST":
        sender = Profile.objects.get(user=request.user)
        receiver = Profile.objects.get(pk=request.POST.get('profile_pk'))
        relationship = Relationship.objects.get((Q(sender=sender) & Q(receiver=receiver)) | (Q(receiver=sender) & Q(sender=receiver)))
        relationship.delete()

        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profiles')

def requests_received(request):
    me = Profile.objects.get(user=request.user)
    rels = Relationship.objects.requests_received(me)
    senders = list(map(lambda x: x.sender, rels))
    is_empty = False
    if len(senders) == 0:
        is_empty = True;
    context = {'senders': senders, 'is_empty': is_empty }
    return render(request, 'accounts/requests_received.html', context)

def accept_request(request):
    if request.method == 'POST':
        sender = Profile.objects.get(pk=request.POST.get('sender_pk'))
        receiver = Profile.objects.get(user=request.user)
        rel = Relationship.objects.get(sender=sender, receiver=receiver)
        if rel.status == 'sent':
            rel.status = 'accepted'
            rel.save()
    return redirect(request.META.get('HTTP_REFERER'))


def remove_request(request):
    if request.method == 'POST':
        sender = Profile.objects.get(pk=request.POST.get('sender_pk'))
        receiver = Profile.objects.get(user=request.user)
        rel = Relationship.objects.get(sender=sender, receiver=receiver)
        rel.delete()
    return redirect(request.META.get('HTTP_REFERER'))


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self, slug=None):
        slug = self.kwargs.get('slug')
        profile = Profile.objects.get(slug=slug)
        return profile
