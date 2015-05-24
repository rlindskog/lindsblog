from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(default='Ryan Lindskog', max_length=50)

    CATEGORY_CHOICES = (
        ('Tech', 'Tech'),
        ('Sports', 'Sports'),
        ('Music', 'Music'),
        ('Philosophy', 'Philosophy'),
        ('Other', 'Other'),
    )

    category = models.CharField(max_length=120, choices=CATEGORY_CHOICES)
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    edited = models.DateTimeField(auto_now_add=False, auto_now=True)

    slug = models.SlugField(max_length=120, unique=True)

    # this is what the table will be labeled in the admin! instead of post object
    def __str__(self):
        return str(self.title)

    # names the object.  also orders stuff.  this is completely optional to do, and I honestly don't like it
    # class Meta:
    #     # verbose_name = "Blog Entry"
    #     # verbose_name_plural = "Blog Entries"
    #     ordering = ['-created']

class Votes(models.Model):
    upvote = models.IntegerField()
    down_vote = models.IntegerField()