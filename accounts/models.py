from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from .utils import random_uuid

class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name  = models.CharField(max_length=100, blank=True)
    last_name   = models.CharField(max_length=100, blank=True)
    avatar      = models.ImageField(default='person.jpg', upload_to="avatars")
    friends     = models.ManyToManyField(User, related_name="friends", blank=True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.user.username}' profile"

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
