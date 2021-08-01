from django.urls import path
from .views import home, about, services

app_name = "InfoPage"

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('services/', services, name="services"),

]