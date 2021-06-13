from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from .utils import random_uuid
from django.db.models import Q

class ProfileManager(models.Manager):
    def other_profiles(self, me):
        profiles    = Profile.objects.all().exclude(user=me)
        return profiles

    def to_friend(self, me):
        myself = Profile.objects.get(user=me)
        profiles    = Profile.objects.all().exclude(user=me)
        relationships = Relationship.objects.filter(Q(sender = myself) | Q(receiver = myself))
        rels = set([])
        for rel in relationships:
            rels.add(rel.sender)
            rels.add(rel.receiver)
        available = [profile for profile in profiles if profile not in rels]

        return available

class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name  = models.CharField(max_length=100, blank=True)
    last_name   = models.CharField(max_length=100, blank=True)
    avatar      = models.ImageField(default='person.jpg', upload_to="avatars")
    friends     = models.ManyToManyField(User, related_name="friends", blank=True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(unique=True, blank=True)

    objects = ProfileManager()

    def __str__(self):
        return f"{self.user.username}' profile"

    def num_of_friends(self):
        return self.friends.all().count()

    def save(self, *args, **kwargs):
        exists = False;
        if self.first_name and self.last_name:
            to_slug=slugify(str(self.first_name) + " " + str(self.last_name))
            exists = Profile.objects.filter(slug=to_slug).exists()
            while exists:
                to_slug += str(random_uuid())
        else:
            to_slug = self.user.username

        self.slug = to_slug
        super().save(*args, **kwargs)


STATUS_CHOICES = [
    ('sent', 'sent'),
    ('accepted', 'accepted')
]
class Relationship(models.Model):
    sender      = models.ForeignKey(Profile, related_name="sender", on_delete=models.CASCADE)
    receiver    = models.ForeignKey(Profile, related_name="receiver", on_delete=models.CASCADE)
    status      = models.CharField(max_length=8,choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.status} - {self.sender} - {self.receiver}"
