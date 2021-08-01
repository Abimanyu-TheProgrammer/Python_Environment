from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk' : self.pk })

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
