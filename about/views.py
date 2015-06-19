from django.shortcuts import render

def about(request):
    template = 'about.html'
    return render(request, template)
# Create your views here.
