from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Service, Booking
from .forms import BookingForm
import datetime

# Define your time slot intervals
TIME_SLOT_INTERVAL = datetime.timedelta(minutes=10)

def generate_time_slots(start_time, end_time):
    slots = []
    current_time = start_time
    while current_time <= end_time:
        slots.append(current_time.strftime("%H:%M"))
        current_time += TIME_SLOT_INTERVAL
    return slots

@login_required
def book_service(request):
    # Time slot range
    start_time = datetime.time(14, 0)
    end_time = datetime.time(21, 30)
    
    available_slots = generate_time_slots(datetime.datetime.combine(datetime.date.today(), start_time),
                                          datetime.datetime.combine(datetime.date.today(), end_time))

    if request.method == 'POST':
        form = BookingForm(request.POST, time_slots=available_slots)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.time_slot = datetime.datetime.strptime(form.cleaned_data['time_slot'], "%H:%M").time()
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm(time_slots=available_slots)

    selected_service_id = request.GET.get('service', None)
    selected_date = request.GET.get('date', None)
    if selected_service_id and selected_date:
        selected_service = Service.objects.get(id=selected_service_id)
        selected_date = datetime.datetime.strptime(selected_date, '%Y-%m-%d').date()
        service_duration = selected_service.duration
        cleaning_time = datetime.timedelta(minutes=10)
        total_time = service_duration + cleaning_time
        
        # Filter existing bookings for the selected date and service
        bookings = Booking.objects.filter(service=selected_service, date=selected_date)
        booked_slots = []
        for booking in bookings:
            booked_start_time = booking.time_slot
            booked_end_time = (datetime.datetime.combine(datetime.date.today(), booked_start_time) + total_time).time()
            current_time = booked_start_time
            while current_time <= booked_end_time:
                booked_slots.append(current_time.strftime("%H:%M"))
                current_time = (datetime.datetime.combine(datetime.date.today(), current_time) + TIME_SLOT_INTERVAL).time()

        available_slots = [slot for slot in available_slots if slot not in booked_slots]

    return render(request, 'booking/book_service.html', {
        'form': form,
        'available_slots': available_slots,
        'selected_service_id': selected_service_id,
        'selected_date': selected_date
    })


@login_required
def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'booking/book_confirmation.html', {'booking': booking})
