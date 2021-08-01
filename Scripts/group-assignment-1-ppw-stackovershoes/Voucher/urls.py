from django.urls import path, include
from django.conf.urls import url
from . import views
from .models import Voucher

app_name = 'Voucher'

urlpatterns = [
    
    path('', views.voucher, name='voucher')
]