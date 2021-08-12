from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    """Creates a post class"""
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return the post by a title"""
        return self.title

    def get_absolute_url(self):
        """Returns the url """
        return reverse('post-detail', kwargs={'pk': self.pk})