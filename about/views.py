from django.shortcuts import render

def about(request):
    template = "about.html"
    render(request, template)
# Create your views here.
