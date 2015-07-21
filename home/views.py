from django.shortcuts import render, get_object_or_404
from django.conf import settings

def template_title(a_request):
    user = a_request.user
    path = a_request.get_full_path()
    if path == '/':
        current_page = 'Home'
    else:
        split_path = path.split('/')
        if len(split_path) > 1:
            current_page = path.split('/')[1].title()
        else:
            current_page = path.split('/')[-1].title()

    if user.is_authenticated():
        title_string = "%s | %s" % (user, current_page)
    else:
        title_string = "Signup! | %s" % current_page
    return title_string

def home(request):
    template = 'home.html'

    context = {
        'title': template_title(request),
    }
    return render(request, template, context)

def about(request):
    template = 'about.html'
    print(template_title(request))
    context = {
        'title': template_title(request),
    }
    template = 'about.html'
    return render(request, template, context)

def portfolio(request):
    template = 'portfolio.html'
    context = {
        'title': template_title(request),
    }

    return render(request, template, context)


def construction(request):
    template = 'construction.html'
    context = {
        'title': template_title(request),
    }
    return render(request, template, context)
