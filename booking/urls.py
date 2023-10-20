from django.urls import path
from .views import book_hotel, hotel_list, check_date_overlap

app_name = 'booking'

urlpatterns = [
    path('book/', hotel_list, name='hotel_list'),
    path('book/<int:hotel_id>/', book_hotel, name='book_hotel'),
    path('check_date_overlap/', check_date_overlap, name='check_date_overlap'),
]
