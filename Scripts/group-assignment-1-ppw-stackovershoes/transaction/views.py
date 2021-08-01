from django.shortcuts import render, redirect
from django.contrib import messages
from django.core import validators
from django.urls import reverse
from django.db.models import Q
# from django.contrib.postgres.search import SearchVector
from homepage.models import Item, Category
from homepage.views import build_url
from Voucher.models import Voucher
from .models import Transaction
from .forms import AddTransaction
import datetime
# code_name, price_cut, minimum_price, expired_date


# Create your views here.
def index(request):
    context = {
        'nav': [
            [build_url('homepage:index'), 'HOME'],
            [build_url('homepage:category'), 'CATEGORY'],
            [build_url('Voucher:voucher'), 'VOUCHERS'],
            [build_url('transaction:history'), 'HISTORY']
        ],
    }

    if request.method == 'GET':
        if request.GET.get('item_id'):
            try:
                item = Items.objects.get(id=request.GET.get('item_id'))
            except Items.DoesNotExist:
                return redirect(build_url('homepage:index'))
            
            context['item'] = item
            context['item_price'] = item.price
            context['item_id'] = item.id
            context['voucher'] = None
            return render(request, 'buy.html', context)
    elif request.method == 'POST':
        context['voucher'] = None
        item = Items.objects.get(id=request.POST.get('item_id'))
        if not request.POST.get('buy') and request.POST.get('voucher'):
            try:
                voucher = Voucher.objects.get(code_name='voucher')
                if datetime.datetime.now() > voucher.expired_date or item.price < voucher.minimum_price:
                    raise Voucher.DoesNotExist

                context['item_price'] = item.price*voucher.price_cut//100
            except Voucher.DoesNotExist:
                return render(request, 'buy.html', context)

            context['item_id'] = item.id
            return render(request, 'buy.html', context)
        elif request.POST.get('buy') == 'TRUE':
            attribute = request.POST
            attribute.pop('buy')

            form = AddTransaction(attribute)
            if form.is_valid():
                form.save()
                return redirect(build_url('transaction:thanks'))            
    
    return redirect(build_url('homepage:index'))

def thanks(request):
    context = {
        'nav': [
            [build_url('homepage:index'), 'HOME'],
            [build_url('homepage:category'), 'CATEGORY'],
            [build_url('Voucher:voucher'), 'VOUCHERS'],
            [build_url('transaction:history'), 'HISTORY']
        ],
    }
    return render(request, 'thanks.html', context)
    

def history(request):
    trans = Transaction.objects.all()

    context = {
        'nav': [
            [build_url('homepage:index'), 'HOME'],
            [build_url('homepage:category'), 'CATEGORY'],
            [build_url('Voucher:voucher'), 'VOUCHERS'],
            [build_url('transaction:history'), 'HISTORY']
        ],
        'history': trans,
    }

    return render(request, 'history.html', context)
