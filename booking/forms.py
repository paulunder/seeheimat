from django import forms
from .models import Booking
from pages.models import Service
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import datetime

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'date', 'time_slot']
        widgets = {
            'date': forms.SelectDateWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Book Now', css_class='btn-primary btn-block'))

        if 'date' in self.data and 'service' in self.data:
            service_id = int(self.data.get('service'))
            date = self.data.get('date')
            if service_id and date:
                service = Service.objects.get(id=service_id)
                date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
                self.fields['time_slot'].choices = self.get_time_slot_choices(service, date)

    def get_time_slot_choices(self, service, date):
        start_time = datetime.time(14, 0) 
        end_time = datetime.time(21, 30)   
        slots = generate_time_slots(start_time, end_time, service.duration)
        booked_slots = Booking.objects.filter(service=service, date=date).values_list('time_slot', flat=True)
        choices = [(slot, slot.strftime('%H:%M')) for slot in slots if slot not in booked_slots]
        return choices

def generate_time_slots(start_time, end_time, service_duration):
    slots = []
    current_time = start_time
    while datetime.datetime.combine(datetime.date.today(), current_time) + service_duration <= datetime.datetime.combine(datetime.date.today(), end_time):
        slots.append(current_time)
        (datetime.datetime.combine(datetime.date.today(), current_time) + service_duration).time()
    return slots
