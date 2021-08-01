from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

context = {}

def home(request):
    return render(request, 'account/home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            context['username'] = username
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form' : form})