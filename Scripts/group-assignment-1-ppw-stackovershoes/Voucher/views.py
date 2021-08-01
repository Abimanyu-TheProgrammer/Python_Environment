from django.shortcuts import render
from .models import Voucher
from homepage.views import build_url

# Create your views here.
def voucher(request):
    context={
        'vouchers': Voucher.objects.all(),
        'nav': [
            [build_url('homepage:index'), 'HOME'],
            [build_url('homepage:category'), 'CATEGORY'],
            [build_url('Voucher:voucher'), 'VOUCHERS'],
            [build_url('transaction:history'), 'HISTORY']
        ],
    }
    return render(request, 'Voucher/voucher.html', context)