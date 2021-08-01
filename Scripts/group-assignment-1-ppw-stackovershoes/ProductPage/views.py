from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from homepage.views import build_url
from homepage.models import Item
# Create your views here.


def Product_Page(request, id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/productpage/' + str(id))

    else:

        item = Item.objects.filter(id = id)[0]
        context = {
            'reviews': Review.objects.all(),
            'item' : item
        }
    return render(request, 'ProductPage/productpage.html', context)