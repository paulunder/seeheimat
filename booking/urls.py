from django.urls import path
from .views import select_date, select_service, book_service, booking_confirmation, get_available_slots

urlpatterns = [
    path('date/', select_date, name='select_date'),
    path('service/<str:selected_date>/', select_service, name='select_service'),
    path('book/<str:selected_date>/<int:selected_service_id>/', book_service, name='book_service'),
    path('slots/', get_available_slots, name='get_available_slots'),
    path('confirmation/<int:booking_id>/', booking_confirmation, name='booking_confirmation'),
]
