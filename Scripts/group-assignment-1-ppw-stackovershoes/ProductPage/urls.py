from django.urls import path, include
from django.conf.urls import url
from . import views
from .models import Review

app_name = 'ProductPage'

urlpatterns = [
    path('', views.Product_Page, name='product_page')
]