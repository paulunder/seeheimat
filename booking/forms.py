from django import forms
from .models import Booking
from pages.models import Service

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'date']
        widgets = {
            'date': forms.SelectDateWidget(),
        }
