from django.shortcuts import render
from .models import Reviews


def home(request):
    return render(request, 'home.html')


def about(request):
    if request.method == 'POST':
        reviews = request.POST.get('reviews')
        new_review = Reviews(text=reviews)
        new_review.save()
    all_reviews = Reviews.objects.all()
    return render(request, 'about.html', {"reviews": all_reviews})


def images(request):
    return render(request, 'images.html')