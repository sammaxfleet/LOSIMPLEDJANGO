from django.urls import path
from .views import (
    book_hotel, hotel_list,
    check_date_overlap, my_books,
    book_edit, delete_book
    )

app_name = 'booking'

urlpatterns = [
    path('book/', hotel_list, name='hotel_list'),
    path('book/<int:hotel_id>/', book_hotel, name='book_hotel'),
    path('check_date_overlap/', check_date_overlap, name='check_date_overlap'),
    path('my_books/', my_books, name='my_books'),
    path('book/<int:book_id>', book_edit, name='book_edit'),
    path('delete_book/<int:book_id>', delete_book, name='delete_book'),
]
