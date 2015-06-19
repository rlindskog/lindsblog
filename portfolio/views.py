from django.shortcuts import render

def portfolio(request):
    template = 'portfolio.html'
    return render(request, template)
# Create your views here.
