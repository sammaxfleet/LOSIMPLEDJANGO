from django.urls import path
from .views import home, about, images, contact_form, contact_success


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('images/', images, name='images'),
    path('contact_form/', contact_form, name='contact_form'),
    path('contact_success/', contact_success, name='contact_success'),
]
