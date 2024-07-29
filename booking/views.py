from django.shortcuts import render, redirect
from .forms import BookingForm

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking')
    else:
        form = BookingForm()
    return render(request, 'booking/booking.html', {'form': form})