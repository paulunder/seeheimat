from django.shortcuts import render, reverse, redirect
from django.views import generic, View
from django.contrib.auth.models import User
import datetime
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator
from .models import Booking
from .forms import BookingForm



def get_user_instance(request):
    """
    gets user details if logged in
    """

    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user


class BookService(View):
    """
    This view will display the booking form
    """
    template_name = 'booking/book_service.html'

    def get(self, request, *args, **kwargs):
        form = BookingForm()
        context = {'booking_form': form}
        if request.user.is_authenticated:
            context['bookings'] = Booking.objects.filter(user=request.user)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(
                request, 'You successfully booked an appointment, it will be confirmed soon.'
                )
            return redirect('confirmed')
        context = {'booking_form': form}
        if request.user.is_authenticated:
            context['bookings'] = Booking.objects.filter(user=request.user)
        return render(request, self.template_name, context)


class Confirmed(generic.DetailView):
    """
    This view will confirm the booking
    """
    template_name = 'booking/book_confirmation.html'

    def get(self, request):
        return render(request, 'booking/book_confirmation.html')


class BookingList(generic.ListView):
    """
    This view will display all the bookings
    """
    model = Booking
    queryset = Booking.objects.filter().order_by('-created_date')
    template_name = 'book_list.html'
    paginated_by = 4

    def get(self, request, *args, **kwargs):

        booking = Booking.objects.all()
        if request.user.is_authenticated:
            user = get_user_instance(request)
            paginator = Paginator(Booking.objects.filter(user=request.user), 4)
        else:
            paginator = Paginator(Booking.objects.all(), 4)
        page = request.GET.get('page')
        booking_page = paginator.get_page(page)
        today = datetime.datetime.now().date()

        for date in booking:
            if date.requested_date < today:
                date.status = 'Booking Expired'

        if request.user.is_authenticated:
            bookings = Booking.objects.filter(user=request.user)
            return render(
                request,
                'booking/book_list.html',
                {
                    'booking': booking,
                    'bookings': bookings,
                    'booking_page': booking_page})
        else:
            return redirect('account_login')


class EditBooking(SuccessMessageMixin, UpdateView):
    """
    This view will allow the user to edit their booking
    """
    model = Booking
    form_class = BookingForm
    template_name = 'booking/book_edit.html'
    success_message = 'Booking has been updated.'


    def get_success_url(self, **kwargs):
        return reverse('booking_list')

def cancel_booking(request, pk):
    """
    This view will allow the user to cancel their booking
    """
    booking = Booking.objects.get(pk=pk)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking cancelled")
        return redirect('booking_list')

    return render(
        request, 'booking/book_cancel.html', {'booking': booking})
