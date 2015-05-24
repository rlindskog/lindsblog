from django.shortcuts import render, get_object_or_404
from .models import Post
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your views here.

def construction(request):
    template = 'construction.html'
    return render(request, template)

# let's make home include all posts, and categories be the only posts
def blog(request):
    entries = Post.objects.all()
    paginator = Paginator(entries, 1)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        entries = paginator.page(page)
    except (InvalidPage, EmptyPage):
        entries = paginator.page(paginator.num_pages)

    # because index is out basic layout
    template = 'index.html'

    content = dict(posts=entries, user=request.user)

    return render(request, template, content)
