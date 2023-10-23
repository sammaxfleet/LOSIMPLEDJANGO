from django.shortcuts import render, get_object_or_404
from .models import Hotel, Booking
from django.http import JsonResponse


def my_books(request):
    my_books = Booking.objects.filter(user=request.user).all()
    allhotels = []
    for book in my_books:
        allhotels.append({
            "name": book.hotel.name,
            "description": book.hotel.description,
            "image": book.hotel.image,
            "price": book.hotel.price,
            "hotel_id": book.hotel.id,
            "book_id": book.id,

        })
    return render(request, 'my_books.html', {'hotels': allhotels})


def hotel_list(request):
    hotels = Hotel.objects.all().order_by('name')
    allhotels = []
    for hotel in hotels:
        allhotels.append({
            "name": hotel.name,
            "description": hotel.description,
            "image": hotel.image,
            "price": hotel.price,
            "id": hotel.id,

        })
    return render(request, 'book.html', {'hotels': hotels})


def book_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    check_in_date = request.POST.get('check_in_date')
    check_out_date = request.POST.get('check_out_date')
    my_books = Booking.objects.filter(user=request.user).all()
    checked_dates = []
    for checked_date in my_books:
        checked_dates.append(checked_date.check_in_date)
        checked_dates.append(checked_date.check_out_date)
    if check_in_date in checked_dates:
        return redirect('book_hotel')
    if request.method == 'POST':

        user = request.user
        booking = Booking(hotel=hotel, user=user,
                          check_in_date=check_in_date, check_out_date=check_out_date)
        booking.save()

        return render(request, 'success.html', {'hotel': hotel, 'booking': booking})

    return render(request, 'booking.html', {'hotel': hotel})


def check_date_overlap(request):
    check_in_date = request.GET.get('check_in_date')
    check_out_date = request.GET.get('check_out_date')

    # Query the database to check for overlapping bookings
    overlapping_bookings = Booking.objects.filter(
        check_in_date__lt=check_out_date,
        check_out_date__gt=check_in_date,
        user=request.user,
    )

    overlap = overlapping_bookings.exists()

    return JsonResponse({'overlap': overlap})
