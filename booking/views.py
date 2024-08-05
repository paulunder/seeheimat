from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Service, Booking
from .forms import BookingForm
import datetime

# Define your time slot intervals
TIME_SLOT_INTERVAL = datetime.timedelta(minutes=10)

def generate_time_slots(start_time, end_time, service_duration):
    slots = []
    current_time = start_time
    while (datetime.datetime.combine(datetime.date.today(), current_time) + service_duration) <= datetime.datetime.combine(datetime.date.today(), end_time):
        slots.append(current_time.strftime('%H:%M'))
        current_time = (datetime.datetime.combine(datetime.date.today(), current_time) + TIME_SLOT_INTERVAL).time()
    return slots

@login_required
def select_date(request):
    if request.method == 'POST':
        selected_date = request.POST.get('date')
        return redirect('select_service', selected_date=selected_date)
    return render(request, 'booking/select_date.html')

@login_required
def select_service(request, selected_date):
    services = Service.objects.all()
    if request.method == 'POST':
        selected_service_id = request.POST.get('service')
        return redirect('book_service', selected_date=selected_date, selected_service_id=selected_service_id)
    return render(request, 'booking/select_service.html', {
        'services': services,
        'selected_date': selected_date,
    })

@login_required
def book_service(request, selected_date, selected_service_id):
    selected_date = datetime.datetime.strptime(selected_date, '%Y-%m-%d').date()
    start_time = datetime.time(14, 0)
    end_time = datetime.time(21, 30)
    selected_service = Service.objects.get(id=selected_service_id)
    service_duration = selected_service.duration

    available_slots = generate_time_slots(start_time, end_time, service_duration)

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

    bookings = Booking.objects.filter(service=selected_service, date=selected_date)
    booked_slots = []
    cleaning_time = datetime.timedelta(minutes=10)
    total_time = service_duration + cleaning_time
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
    return render(request, 'booking/booking_confirmation.html', {'booking': booking})

def get_available_slots(request):
    date_str = request.GET.get('date')
    if not date_str:
        return JsonResponse({'error': 'Invalid date'}, status=400)
    
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    
    # Define start and end time for the slots and the duration
    start_time = datetime.time(14, 0)  # 2:00 PM
    end_time = datetime.time(21, 30)   # 9:30 PM

    # Get all time slots
    all_slots = generate_time_slots(start_time, end_time, datetime.timedelta(minutes=30))
    
    # Get unavailable time slots based on current bookings
    booked_slots = Booking.objects.filter(date=date).values_list('time_slot', flat=True)
    booked_slots = [slot.strftime('%H:%M') for slot in booked_slots]
    
    available_slots = [slot for slot in all_slots if slot not in booked_slots]
    
    return JsonResponse({
        'available_slots': available_slots,
        'booked_slots': booked_slots
    })
