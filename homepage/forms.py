from django import forms #Luis april 19 I js wanted to strat it off and for u to later on check it and see if its good. I know we probaby have to add more to the rest of the code so it can link but i didnt wanna go ahead and do that before u reviewed this. 
from .models import Registration, Review

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'subject', 'message']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['laptop', 'rating', 'comment']
