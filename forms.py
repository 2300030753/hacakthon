from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']


# forms.py
from django import forms
from .models import EventBooking

class BookingForm(forms.ModelForm):
    class Meta:
        model = EventBooking
        fields = ['event_name', 'name', 'email', 'phone']
        widgets = {
            'event_name': forms.HiddenInput(),
        }
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comments']
        widgets = {
            'rating': forms.NumberInput(attrs={
                'min': 1,
                'max': 5,
                'placeholder': 'Rate between 1 and 5'
            }),
            'comments': forms.Textarea(attrs={
                'placeholder': 'Share your comments here...',
                'rows': 4,
                'cols': 50
            }),
        }
        labels = {
            'rating': 'Rating (1-5)',
            'comments': 'Comments',
        }