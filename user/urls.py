from django.urls import path
from . import views

urlpatterns = [
    # Other URLs
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout_view/', views.logout_view, name='logout_view'),
]
