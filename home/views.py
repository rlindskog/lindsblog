from django.shortcuts import render, get_object_or_404
from django.conf import settings

def home(request):
    template = 'home.html'
    return render(request, template)


# Create your views here.
