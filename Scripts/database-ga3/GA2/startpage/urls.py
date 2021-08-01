from django.urls import path
from .views import itemForm,readItem,deleteLaundryList,updateLaundryList,laundryListForm,readLaundryList, topUp, topUpForm, home, deleteTopup, updateTopup, readService, readTestimony, deleteTestimony, testimonyForm, statusRead, updateTestimony, updateService

app_name = "startpage"


urlpatterns = [
    path('', home, name="home"),
    path('topup/', topUp, name="topup"),
    path('topupForm/', topUpForm, name="topUpForm"),
    path('deleteTopup/<email>/<date>/', deleteTopup, name="delete_topUp"),
    path('updateTopup/<email>/<date>/', updateTopup, name="update_topUp"),
    path('testimony/', readTestimony, name="testimony"),
    path('testimonyForm/', testimonyForm, name="testimonyForm"),
    path('deleteTestimony/<email>/<date>/', deleteTestimony, name="delete_testimony"),
    path('updateTestimony/<email>/<date>/', updateTestimony, name="update_testimony"),
    path('service/', readService, name="service"),
    path('status/', statusRead, name="status"),
    path('updateService/<code>/', updateService, name="update_service"),
    path('laundryList/', readLaundryList, name="laundryList"),
    path('laundryListForm/', laundryListForm, name="laundryListForm"),
    path('updateLaundryList/<email>/<date>/', updateLaundryList, name="updateLaundryList"),
    path('deleteLaundryList/<email>/<date>/', deleteLaundryList, name="deleteLaundryList"),
    path('item/', readItem, name="item"),
    path('item_user/', readItem, name="item2"),
    path('itemForm/', itemForm, name="itemForm"),
]