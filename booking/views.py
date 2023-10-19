from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Hotel, Booking


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
