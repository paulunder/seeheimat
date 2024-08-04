from django.contrib import admin

from booking.models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'date', 'time_slot')
    search_fields = ['user', 'service']
    list_filter = ('date', 'time_slot')
