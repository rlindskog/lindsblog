from django.shortcuts import render

def portfolio(request):
    template = "portfolio.html"
    render(request, template)
# Create your views here.
