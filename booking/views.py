import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from pages.models import Service
from .models import Booking
from .forms import BookingForm

TIME_SLOTS = [
    "14:00", "14:10", "14:20", "14:30", "14:40", "14:50",
    "15:00", "15:10", "15:20", "15:30", "15:40", "15:50",
    "16:00", "16:10", "16:20", "16:30", "16:40", "16:50",
    "17:00", "17:10", "17:20", "17:30", "17:40", "17:50",
    "18:00", "18:10", "18:20", "18:30", "18:40", "18:50",
    "19:00", "19:10", "19:20", "19:30", "19:40", "19:50",
    "20:00", "20:10", "20:20", "20:30", "20:40", "20:50",
    "21:00", "21:10", "21:20", "21:30"
]

@login_required
def book_service(request):
    available_slots = TIME_SLOTS.copy()
    selected_service_id = request.GET.get('service', None)
    selected_date = request.GET.get('date', None)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.time_slot = request.POST.get('time_slot')
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()

    if selected_service_id and selected_date:
        selected_service = Service.objects.get(id=selected_service_id)
        selected_date = datetime.datetime.strptime(selected_date, '%Y-%m-%d').date()
        service_duration = selected_service.duration
        cleaning_time = datetime.timedelta(minutes=10)  # 10 minutes for cleaning
        total_time = service_duration + cleaning_time

        bookings = Booking.objects.filter(service=selected_service, date=selected_date)

        for booking in bookings:
            booked_start_time = booking.time_slot
            booked_start_datetime = datetime.datetime.combine(datetime.date.today(), booked_start_time)
            booked_end_datetime = booked_start_datetime + total_time
            current_time = booked_start_datetime
            while current_time < booked_end_datetime:
                time_str = current_time.time().strftime("%H:%M")
                if time_str in available_slots:
                    available_slots.remove(time_str)
                current_time += datetime.timedelta(minutes=10)

    return render(request, 'booking/book_service.html', {
        'form': form,
        'available_slots': available_slots,
        'selected_service_id': selected_service_id,
        'selected_date': selected_date
    })

@login_required
def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'booking/booking_confirmation.html', {'booking': booking})
