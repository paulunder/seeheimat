from django.urls import path
from .views import book_service, booking_confirmation

urlpatterns = [
    path('booking/', book_service, name='book_service'),
    path('confirmation/<int:booking_id>/', booking_confirmation, name='booking_confirmation'),
]