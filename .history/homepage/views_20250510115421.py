from datetime import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader

from homepage.forms import RegistrationForm

# Create your views here.

def index(request): 
    return render(request, "homepage/index.html")

def about(request): 
    return render(request, "homepage/about.html")

def contact(request): 
    return render(request, "homepage/contact.html")


def support(request): 
    return render(request, "homepage/support.html")

def review_form(request): 
    form = RegistrationForm(request.POST or None)

    if request.method == "POST": 
        if form.is_valid(): 
            message = form.save(commit=False) 
            message.log_date = datetime.now() 
            message.save() 
            return redirect("support")
        
        else: 
            return render(request, "homepage/support.html", {"form":form})

    return render(request, "homepage/support.html", {"form":form})



