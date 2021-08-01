from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'transaction'

urlpatterns = [
    path('', views.index, name='index'),
    path('thanks/', views.thanks, name="thanks"),
    path('history/', views.history, name="history")
]