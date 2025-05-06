from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import ReviewForm, RegistrationForm, LaptopForm

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

def feedback_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # after submitting feedback
    else:
        form = ReviewForm()
    return render(request, 'homepage/feedback.html', {'form': form})




