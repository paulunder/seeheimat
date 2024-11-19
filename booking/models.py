from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from pages.models import Service

# Working hours of the massage service
time_slots = (
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('19:00', '19:00'),
    ('20:00', '20:00'),
    ('21:00', '21:00'),
)


# Status options
status_options = (
    ('Awaiting confirmation', 'Awaiting Confirmation'),
    ('Booking Confirmed', 'Booking Confirmed'),
    ('Booking Rejected', 'Booking Rejected'),
    ('Booking Expired', 'Booking Expired'),
)

# The booking model for the database
class Booking(models.Model):
    """
    the class for the booking model which is used to handle the bookings
    """
    booking_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    requested_date = models.DateField()
    requested_time = models.CharField(
        max_length=25,
        choices=time_slots,
        default='14:00'
        )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="service_reserved",
        null=True
        )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", null=True)
    name = models.CharField(
        max_length=50,
        null=True
        )
    email = models.EmailField(
        max_length=254,
        default=""
        )
    status = models.CharField(
        max_length=25,
        choices=status_options,
        default='awaiting confirmation'
        )

    class Meta:
        ordering = ['-requested_time']
        unique_together = ('requested_date', 'requested_time')

    def __str__(self):
        return self.status