from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('service', 'date', 'time_slot')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time_slot': forms.Select(attrs={'class': 'form-control'})
        }