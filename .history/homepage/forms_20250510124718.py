from django import forms
from .models import Product, Feedback

# feedback form
class Feedback(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'description': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'image': forms.Textarea(attrs={'class': 'form-control'}),
        }

# Product form (THIS is the one for users to review laptops)
class Product(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['laptop', 'rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your thoughts here...'}),
        }


     