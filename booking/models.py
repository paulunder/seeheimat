from datetime import timezone
from django.conf import settings
from django.db import models

from pages.models import Service

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default= 1)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default=1)
    date = models.DateField()
    time = models.TimeField(default="14:30")
    created_at = models.DateTimeField(default="2024-07-30 14:30")

    def __str__(self):
        return f'{self.service.name} booking by {self.user.username} on {self.date} at {self.time}'
