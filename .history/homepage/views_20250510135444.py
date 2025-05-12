from datetime import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import Product
from homepage.forms import ProductForm, FeedbackForm



# Create your views here.

def index(request): 
    return render(request, "homepage/index.html")

def about(request): 
    return render(request, "homepage/about.html")

def contact(request): 
    return render(request, "homepage/contact.html")


def support(request): 
    form = ProductForm()
    return render(request, "homepage/support.html", {"form": form})


#contact
def review_form(request): 
    form = ProductForm(request.POST or request.FILES or None)

    if request.method == "POST": 
        if form.is_valid(): 
            message = form.save(commit=False) 
            message.log_date = datetime.now() 
            message.save() 
            return redirect("support")
        
        else: 
            return render(request, "homepage/support.html", {"form":form})

    return render(request, "homepage/support.html", {"form":form})

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # after submitting feedback
    else:
        form = FeedbackForm()
    return render(request, 'homepage/feedback.html', {'form': form})




def product_list(request):
    products = Product.objects.all()
    return render(request, 'homepage/index.html', {'products': products})