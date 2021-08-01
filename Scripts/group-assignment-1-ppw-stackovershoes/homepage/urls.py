from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('items/', views.items, name='items')
]