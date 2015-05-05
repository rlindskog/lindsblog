from django.shortcuts import render, get_object_or_404
from .models import Post
from django.conf import settings
# Create your views here.

def construction(request):
    template = 'construction.html'
    return render(request, template)

def home(request):
    return render(request)

def about(request):
    return render(request)

def contact(request):
    return render(request)


def blog(request):
    entries = Post.objects.all()[:10]

    template = 'blog.html'
    # title_view = "this should be a model title"
    # author_view = "this should be a model author"
    # category_view = "this should be a model category"
    # body_view = "this should be a model body ;)"
    # created_view = "this should be a model created"

    # content = dict(title=title_view, author=author_view, category=category_view, body=body_view, created=created_view)
    content = dict(posts=entries)

    return render(request, template, content)
