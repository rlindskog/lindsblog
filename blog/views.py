from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from home.views import template_title

from .models import Post
from .forms import CategoryForm

from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your views here.

# let's make home include all posts, and categories be the only posts

def blog(request):

    form = CategoryForm(request.POST or None)

    if form.is_valid():
        category = form.cleaned_data.get('category')
    else:
        category = 'All'

    print(category)

        # if Post.objects.filter(title="First"):
        #     print("There is at least one entry called first.")

    entries = Post.objects.order_by("-created").all()  # order_by("-created") to reverse

    entry_list = list(entries)
    paginator = Paginator(entries, 12)
    for i in entries:
        print(i.created)

    try:
        page = int(request.GET.get("page", '1')) # this is where you set beginning page!  If you want it to start from last, page = paginator.num_pages
    except ValueError:
        page = 1

    try:
        entries = paginator.page(page)
    except (InvalidPage, EmptyPage):
        entries = paginator.page(paginator.num_pages)

    template = 'blog.html'
    context = dict(posts=entries, user=request.user, form=form, category=category, title=template_title(request))

    return render(request, template, context)