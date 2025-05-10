from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request): 
    context = {"Apple_Products": "MacBook Pro"}
    return render(request, "homepage/index.html", context)

def about(request): 
    context = {"name": "Karim Mohamed"} 
    return render(request, "homepage/about.html",context)

def contact(request): 
    context = {"Email": "example@gmail.com"} 
    return render(request, "homepage/contact.html", context)



