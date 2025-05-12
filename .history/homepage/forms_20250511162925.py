from django import forms
from .models import Feedback


# Product form (THIS is the one for users to review laptops)
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'product', 'rating', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comment': forms.Textarea(attrs={'rows': 3, 'cols':40, 'placeholder': 'Message'}),
        }


     
