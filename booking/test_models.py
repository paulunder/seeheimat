from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date, timedelta
from pages.models import Service
from .models import Booking


class BookingModelTest(TestCase):
    """
    Test the booking model
    """

    def setUp(self):
        """
        Set up initial data for tests
        """
        # Create a user
        self.user = User.objects.create_user(
            username='testuser', password='testpass')

        # Create a service
        self.service = Service.objects.create(
            name='Test Service',
            description='Test description',
            duration=timedelta(minutes=60), price=50.00)

        # Create a booking
        self.booking = Booking.objects.create(
            requested_date=date.max,
            requested_time='14:00',
            service=self.service,
            user=self.user,
            name='Test User',
            email='testuser@example.com',
            status='Awaiting confirmation'
        )

    def test_booking_creation(self):
        """
        Test that a booking is correctly created
        """
        self.assertEqual(self.booking.requested_time, '14:00')
        self.assertEqual(self.booking.service, self.service)
        self.assertEqual(self.booking.user, self.user)
        self.assertEqual(self.booking.name, 'Test User')
        self.assertEqual(self.booking.email, 'testuser@example.com')
        self.assertEqual(self.booking.status, 'Awaiting confirmation')

    def test_booking_str(self):
        """
        Test the string representation of the booking
        """
        self.assertEqual(str(self.booking), 'Awaiting confirmation')

    def test_booking_unique_together(self):
        """
        Test the unique constraint on requested_date, requested_time & service
        """
        with self.assertRaises(Exception):
            Booking.objects.create(
                requested_date=self.booking.requested_date,
                requested_time=self.booking.requested_time,
                service=self.service,
                user=self.user,
                name='Another User',
                email='anotheruser@example.com',
                status='Awaiting confirmation'
            )

    def test_default_status(self):
        """
        Test the default status of a booking
        """
        booking = Booking.objects.create(
            requested_date=date.today(),
            requested_time='15:00',
            service=self.service,
            user=self.user,
            name='Default Status User',
            email='defaultstatus@example.com'
        )
        self.assertEqual(booking.status, 'awaiting confirmation')

    def test_ordering(self):
        """
        Test the ordering of bookings by requested_time in descending order
        """
        earlier_booking = Booking.objects.create(
            requested_date=date.today(),
            requested_time='12:00',
            service=self.service,
            user=self.user,
            name='Test User',
            email='testuser@example.com',
            status='Awaiting confirmation'
        )
        bookings = Booking.objects.all()
        self.assertEqual(bookings.first(), self.booking)
        self.assertEqual(bookings.last(), earlier_booking)
