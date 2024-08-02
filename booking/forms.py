from django import forms
from .models import Booking
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Book Now', css_class='btn-primary btn-block'))