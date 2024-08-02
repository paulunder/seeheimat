from django import forms
from .models import Booking
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'time']
        widgets = {
            'time': forms.TextInput(attrs={'class': 'form-control datetimepicker-input', 'data-target': '#datetimepicker1'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.template = 'bootstrap5'  # Specify the template for Bootstrap 5
        self.helper.add_input(Submit('submit', 'Book Now', css_class='btn-primary btn-block'))
