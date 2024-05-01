from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# Create your views here.
def login_user(request):
    if request.method =='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username Or Password Is Incorrect, Try again...!')
            return redirect('login')

    return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Logged Out! Please Log In again...!')
    return redirect('login')

    
# def register_user(request):
#     form =RegisterUserForm()
#     context = {'form': form}
#     return render(request, 'authenticate/register.html', context)


def register_user(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
        # else:
        #     messages.info(request, 'There was an error registering, Try again...!')
        #     return redirect('register')
    context = {'form': form}
    return render(request, 'authenticate/register.html', context)
