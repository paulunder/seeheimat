import datetime
from django.db import models
from django.contrib.auth.models import User
from pages.models import Service

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField(default=datetime.time(14, 0))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('date', 'time_slot', 'service')

    def __str__(self):
        return f"{self.user} - {self.service} at {self.time_slot} on {self.date}"

