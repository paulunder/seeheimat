# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import SimpleTestCase
from django.urls import reverse, resolve
# Internal:
from booking import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestBookingUrls(SimpleTestCase):

    def test_confirmed_url_resolves(self):
        url = reverse('confirmed')
        self.assertEqual(resolve(url).func.view_class, views.Confirmed)

    def test_booking_list_url_resolves(self):
        url = reverse('booking_list')
        self.assertEqual(resolve(url).func.view_class, views.BookingList)

    def test_edit_booking_url_resolves(self):
        url = reverse('edit_booking', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.EditBooking)

    def test_book_cancel_url_resolves(self):
        url = reverse('book_cancel', args=[1])
        self.assertEqual(resolve(url).func, views.cancel_booking)

    def test_book_service_url_resolves(self):
        url = reverse('book_service')
        self.assertEqual(resolve(url).func.view_class, views.BookService)
