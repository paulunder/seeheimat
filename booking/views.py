from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import time, timedelta, datetime
from .models import Service, Booking
from .forms import BookingForm

def generate_time_slots(start_time, end_time, service_duration):
    slots = []
    current_time = start_time
    while datetime.combine(datetime.today(), current_time) + service_duration <= datetime.combine(datetime.today(), end_time):
        slots.append(current_time)
        current_time = (datetime.combine(datetime.today(), current_time) + service_duration).time()
    return slots

@login_required
def book_service(request):
    service_duration = timedelta(minutes=30)  # Duration of the service
    start_time = time(14, 0)  # Start time for booking
    end_time = time(21, 30)   # End time for booking
    all_slots = generate_time_slots(start_time, end_time, service_duration)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()

    booked_slots = Booking.objects.filter(date=request.POST.get('date')).values_list('time_slot', flat=True)
    available_slots = [slot for slot in all_slots if slot not in booked_slots]

    return render(request, 'booking/book_service.html', {
        'form': form,
        'available_slots': available_slots,
    })

@login_required
def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'booking/booking_confirmation.html', {'booking': booking})
