from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, SellerRegisterForm
import phonenumbers

# Create your views here.

def registerUser(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        print(request.POST)
    else:
        form = UserRegisterForm()
    return render(request, 'account/registerUser.html', {'form':form})

def registerSeller(request):
    if request.method == "POST":
        form = SellerRegisterForm(request.POST)
        print(request.POST)
    else:
        form = SellerRegisterForm()
    return render(request, 'account/registerSeller.html', {'form':form})

