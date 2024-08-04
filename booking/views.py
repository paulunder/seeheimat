from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import time, timedelta, datetime
from .models import Service, Booking
from .forms import BookingForm

def generate_time_slots(start_time, end_time, service_duration):
    slots = []
    current_time = datetime.combine(datetime.today(), start_time)
    while current_time.time() < end_time:
        slots.append(current_time.time())
        current_time += service_duration
    return slots

@login_required
def book_service(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()
    
    selected_service_id = request.GET.get('service', None)
    available_slots = []
    booked_slots = []
    
    if selected_service_id:
        try:
            selected_service = Service.objects.get(id=selected_service_id)
            service_duration = selected_service.duration
            start_time = time(14, 0)
            end_time = time(21, 30)
            available_slots = generate_time_slots(start_time, end_time, service_duration)
            
            booked_slots = Booking.objects.filter(service=selected_service, date=form['date'].value()).values_list('time_slot', flat=True)
            available_slots = [slot for slot in available_slots if slot not in booked_slots]
        except Service.DoesNotExist:
            pass
    
    return render(request, 'booking/book_service.html', {
        'form': form,
        'available_slots': available_slots,
        'booked_slots': booked_slots
    })

@login_required
def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'booking/booking_confirmation.html', {'booking': booking})
