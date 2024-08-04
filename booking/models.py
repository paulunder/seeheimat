from django.db import models
from django.contrib.auth.models import User
from pages.models import Service
import datetime

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField()

    def __str__(self):
        return f'{self.service.name} booking for {self.user.username} on {self.date} at {self.time_slot}'
