from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    if request.method == 'POST':
        reviews = request.POST.get('reviews')
        print(reviews)
    return render(request, 'about.html')
