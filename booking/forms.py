from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    time_slot = forms.ChoiceField(choices=[], required=True, widget=forms.RadioSelect)  # Use RadioSelect to display time slots as buttons

    class Meta:
        model = Booking
        fields = ['service', 'date', 'time_slot'] 
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        time_slots = kwargs.pop('time_slots', [])
        super().__init__(*args, **kwargs)
        self.fields['time_slot'].choices = [(slot, slot) for slot in time_slots]
