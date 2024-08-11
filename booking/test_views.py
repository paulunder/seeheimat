# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from datetime import datetime, timedelta

from pages.models import Service
# Internal:
from .models import Booking
from .forms import BookingForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class BookingViewsTestCase(TestCase):
    """
    Tests for the views in the booking app
    """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='password', email='test@example.com')
        self.client.login(username='testuser', password='password')

        self.booking = Booking.objects.create(
            user=self.user,
            requested_date=datetime.now().date(),
            status='Pending'
        )

    def test_book_service_get(self):
        """
        Test the book_service view
        """
        response = self.client.get(reverse('book_service'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/book_service.html')
        self.assertContains(response, 'form')

    def test_book_service_post_valid(self):
        form_data = {
            'name': 'Test Booking',
            'email': 'testuser@example.com',
            'service': Service.objects.create(
                name='Test Service', description='Test description',
                duration=timedelta(minutes=60), price=50.00).pk,
            'requested_date': (
                datetime.now().date() + timedelta(days=1)).isoformat(),
            'requested_time': '14:00'
        }
        response = self.client.post(reverse('book_service'), form_data)
        self.assertRedirects(response, reverse('confirmed'))

    def test_book_service_post_invalid(self):
        """
        Test the book_service view with invalid data
        """
        form_data = {'': '', 'field2': ''}  # Adjust with invalid data
        response = self.client.post(reverse('book_service'), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/book_service.html')

    def test_confirmed_view(self):
        """
        Test the confirmed view
        """
        response = self.client.get(reverse('confirmed'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/book_confirmation.html')

    def test_booking_list_view_authenticated(self):
        """
        Test the booking_list view when the user is authenticated
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('booking_list'))
        # Check for the 'My Bookings' heading
        self.assertContains(response, 'My Bookings')

    def test_booking_list_view_unauthenticated(self):
        """
        Test the booking_list view when the user is not authenticated
        """
        self.client.logout()
        response = self.client.get(reverse('booking_list'))
        self.assertRedirects(response, reverse('account_login'))

    def test_edit_booking_get(self):
        """
        Test the edit_booking view
        """
        response = self.client.get(reverse('edit_booking', args=[
            self.booking.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/book_edit.html')
        self.assertContains(response, 'form')

    def test_cancel_booking_get(self):
        """
        Test the cancel_booking view
        """
        response = self.client.get(reverse('book_cancel', args=[
            self.booking.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/book_cancel.html')

    def test_cancel_booking_post(self):
        """
        Test the cancel_booking view with a POST request
        """
        response = self.client.post(reverse('book_cancel', args=[
            self.booking.pk]))
        self.assertRedirects(response, reverse('booking_list'))
        self.assertFalse(Booking.objects.filter(pk=self.booking.pk).exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Booking cancelled")
