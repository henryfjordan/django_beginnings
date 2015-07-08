from django.db import models
from django_beginnings.users.models import User

# Create your models here.

class BlogPost(models.Model):

    author = models.ForeignKey(User)
    title = models.CharField(max_length=500)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BlogComment(models.Model):

    author