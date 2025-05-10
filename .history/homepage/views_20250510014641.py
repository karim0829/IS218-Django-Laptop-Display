from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request): 
    return render(request, "homepage/index.html")

def about(request): 
    return render(request, "homepage/about.html")

def contact(request): 
    return render(request, "homepage/contact.html")


def support(request): 
    return render(request, "homepage/support.html")




