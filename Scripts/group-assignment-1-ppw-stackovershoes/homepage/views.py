from django.shortcuts import render, redirect
from django.contrib import messages
from django.core import validators
from django.urls import reverse
from django.db.models import Q
# from django.contrib.postgres.search import SearchVector
from .models import Item, Category
from django.http import QueryDict


# Create your views here.
# https://stackoverflow.com/questions/9585491/how-do-i-pass-get-parameters-using-django-urlresolvers-reverse
def build_url(*args, **kwargs):
    params = kwargs.pop('params', {})
    url = reverse(*args, **kwargs)

    if not params:
        return url

    qdict = QueryDict('', mutable=True)
    for k, v in params.items():
        if type(v) is list:
            qdict.setlist(k, v)
        else:
            qdict[k] = v

    return url + '?' + qdict.urlencode()


def index(request):
    all_items = Item.objects.all()
    
    context = {
        'title': 'Homepage',
        'nav': [
            [build_url('homepage:index'), 'HOME'],
            [build_url('homepage:category'), 'CATEGORY'],
            [build_url('Voucher:voucher'), 'VOUCHERS'],
            [build_url('transaction:history'), 'HISTORY']
        ],
        'all_items': all_items,
    }
    return render(request, 'home.html', context)

def category(request):
    context = {
        'title': 'Category',
        'nav': [
            [build_url('homepage:index'), 'HOME'],
            [build_url('homepage:category'), 'CATEGORY'],
            [build_url('Voucher:voucher'), 'VOUCHERS'],
            [build_url('transaction:history'), 'HISTORY']
        ],
        'category': [
            [build_url('homepage:items', params={'category': 'Sports'}), 'Sports'],
            [build_url('homepage:items', params={'category': 'Running'}), 'Running'],
            [build_url('homepage:items', params={'category': 'Casual'}), 'Casual'],
        ]
    }
    return render(request, 'category.html', context)

def items(request):
    context = {
        'title': 'Items',
        'nav': [
            [build_url('homepage:index'), 'HOME'],
            [build_url('homepage:category'), 'CATEGORY'],
            [build_url('Voucher:voucher'), 'VOUCHERS'],
            [build_url('transaction:history'), 'HISTORY']
        ],
    }

    if request.method == 'GET':
        if request.GET.get('category'):
            try:
                category = Category.objects.get(name=request.GET.get('category'))
            except Category.DoesNotExist:
                return redirect(build_url('homepage:category'))
            
            all_items = Item.objects.filter(category=category)
            context['all_items'] = all_items

            return render(request, 'items.html', context)
        # https://learndjango.com/tutorials/django-search-tutorial
        if request.GET.get('search'):
            # Try to use this when deploying to Heroku, uses PostgreSQL
            # all_items = Items.objects.annotate(
            #     search=SearchVector('id', 'name', 'category', 'description')
            # ).filter(search=request.GET.get('search'))

            # Use this when testing locally, uses SQLite
            query = request.GET.get('search')
            all_items = Item.objects.filter(
                Q(id__icontains=query) |
                Q(name__icontains=query) |
                Q(category__name__icontains=query) |
                Q(description__icontains=query)
            )
            context['all_items'] = all_items

            return render(request, 'items.html', context)
    
    return redirect(build_url('homepage:index'))
