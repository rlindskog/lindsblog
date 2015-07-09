from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

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
    paginator = Paginator(entries, 10)

    try:
        page = int(request.GET.get("page", '10'))
    except ValueError:
        page = 1

    try:
        entries = paginator.page(page)
    except (InvalidPage, EmptyPage):
        entries = paginator.page(paginator.num_pages)

    # because index is out basic layout
    template = 'index.html'

    context = dict(posts=entries, user=request.user)

    # # filtering through categories!
    # for post in entries:
    #     if sort_category == 'All':
    #         print(post.title)
    #     else:
    #         if sort_category == 'Tech' and post.category == 'Tech':
    #             print(post.title)
    #         elif sort_category == 'Sports' and post.category == 'Sports':
    #             print(post.title)
    #         elif sort_category == 'Music' and post.category == 'Music':
    #             print(post.title)
    #         elif sort_category == 'Philosophy' and post.category == 'Philosophy':
    #             print(post.title)
    #         elif sort_category == 'Other' post.category == 'Other':
    #             print(post.title)

    return render(request, template, context)