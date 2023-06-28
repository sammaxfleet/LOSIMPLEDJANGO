from django.shortcuts import render, redirect
from .models import Reviews
from .forms import ContactForm


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


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})


def contact_success(request):
    return render(request, 'contact_success.html')
