from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):
    if request.method == 'POST':

        username = request.POST.get('username', '')
        password = request.POST.get('password1', '')
        email = request.POST.get('email', '')
        if User.objects.filter(username=username, email=email).first():
            return redirect('home')
        user = User(username=username, email=email, password=password)
        user.save()
        authenticate(username=username, password=password)
        login(request, user)

        return redirect('home')

    return render(request, 'register.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def myprofile(request):
    user_profile = request.user
    user = {"username": user_profile.username, "email": user_profile.email}

    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        user_profile.username = username
        user_profile.email = email
        user_profile.save()
        return redirect('myprofile')

    return render(request, 'myprofile.html', {"user": user})


def delete_my_profile(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)

        return redirect('home')
    else:
        redirect('home')
