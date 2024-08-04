import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm
from pages.models import Service

def generate_time_slots(start_time, end_time, interval_minutes=10):
    slots = []
    current_time = datetime.datetime.combine(datetime.date.today(), start_time)
    end_datetime = datetime.datetime.combine(datetime.date.today(), end_time)
    while current_time <= end_datetime:
        slots.append(current_time.time())
        current_time += datetime.timedelta(minutes=interval_minutes)
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
            cleaning_time = datetime.timedelta(minutes=10)  # 10 minutes for cleaning
            total_time = service_duration + cleaning_time

            start_time = datetime.time(14, 0)
            end_time = datetime.time(21, 30)
            all_slots = generate_time_slots(start_time, end_time)
            
            bookings = Booking.objects.filter(service=selected_service, date=form['date'].value())
            for booking in bookings:
                booked_start_time = booking.time_slot
                booked_end_time = (datetime.datetime.combine(datetime.date.today(), booked_start_time) + total_time).time()
                slot_time = datetime.datetime.combine(datetime.date.today(), start_time)
                while slot_time.time() < booked_end_time:
                    booked_slots.append(slot_time.time())
                    slot_time += datetime.timedelta(minutes=10)

            available_slots = [slot for slot in all_slots if slot not in booked_slots]
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
