from django import forms
from .models import Registration, Review, Laptop

# Contact form
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'subject', 'message']

# Feedback form (THIS is the one for users to review laptops)
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['laptop', 'rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your thoughts here...'}),
        }
