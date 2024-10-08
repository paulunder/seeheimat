from django.urls import path
from booking import views

# Urls for the booking app
urlpatterns = [
    path('confirmed', views.Confirmed.as_view(), name='confirmed'),
    path('booking_list', views.BookingList.as_view(), name='booking_list'),
    path('edit_booking/<int:pk>',
         views.EditBooking.as_view(), name='edit_booking'),
    path('book_cancel/<int:pk>',
         views.cancel_booking, name='book_cancel'),
    path('book-service/', views.BookService.as_view(), name='book_service'),
]
