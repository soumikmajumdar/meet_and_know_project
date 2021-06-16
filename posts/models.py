from django.db import models
from accounts.models import Profile
from django.core.validators import FileExtensionValidator

class Post(models.Model):
    content     = models.TextField()
    author      = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image       = models.ImageField(validators=[FileExtensionValidator(['jpg'], ['png'], ['jpeg'])], blank=True)
    likes       = models.ManyToManyField(Profile, blank=True, related_name='likes')
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.content[:20]} - {self.author}"

    def num_likes(self):
        return self.likes.all().count()

    def get_all_comments(self):
        return self.comment_set.all()


class Comment(models.Model):
    content     = models.TextField()
    author      = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post        = models.ForeignKey(Post, on_delete=models.CASCADE)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.content[:20]} - {self.author}"

LIKE_STATUS = (
    ('like', 'like'),
    ('unlike', 'unlike')
)

class Like (models.Model):
    post    = models.ForeignKey(Post, on_delete=models.CASCADE)
    user    = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status  = models.CharField(max_length=6, choices=LIKE_STATUS, blank=True)

    def __str__(self):
        return f"{self.status} - {self.user}"
