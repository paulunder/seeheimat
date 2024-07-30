from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Service, Booking
from .forms import BookingForm

# @login_required
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
    return render(request, 'booking/book_service.html', {'form': form})

# @login_required
def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'booking/booking_confirmation.html', {'booking': booking})
