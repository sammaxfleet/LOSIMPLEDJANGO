from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Hotel, Booking


def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'book.html', {'hotels': hotels})


def book_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)

    if request.method == 'POST':
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')
        user = request.user  # Assuming user authentication is implemented
        booking = Booking(hotel=hotel, user=user,
                          check_in_date=check_in_date, check_out_date=check_out_date)
        booking.save()

        return render(request, 'success.html', {'hotel': hotel, 'booking': booking})

    return render(request, 'booking.html', {'hotel': hotel})
