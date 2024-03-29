from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def home(request):
    if request.method == 'POST':
        # Check to see if logging in
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.error(request, 'There was an error logging in, please try again...')
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect(reverse('home'))


def register_user(request):
    return render(request, 'register.html', {})
