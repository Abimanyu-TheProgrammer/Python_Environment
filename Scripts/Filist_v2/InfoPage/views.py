from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, "InfoPage/home.html")

def about(request):
    return render(request, "InfoPage/about.html")

def services(request):
    return render(request, "InfoPage/services.html")



