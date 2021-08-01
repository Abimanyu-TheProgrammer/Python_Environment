from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from homepage.views import build_url
# Create your views here.


def Product_Page(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/productpage/')

    else:
        context ={
            'reviews':Review.objects.all()
        }
    return render(request, 'ProductPage/productpage.html', context)