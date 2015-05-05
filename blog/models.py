from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(default='Ryan', max_length=50)
    category = models.CharField(max_length=120)

    body = models.TextField()


    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

class Votes(models.Model):
    upvote = models.IntegerField()
    down_vote = models.IntegerField()