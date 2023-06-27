from django.urls import path
from .views import home, about, images


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('images/', images, name='images'),
]
