from django.contrib import admin
from .models import DpayTopUpTransaction, Service, Testimony, Status, LaundryList, Item

# Register your models here.
admin.site.register(DpayTopUpTransaction)
admin.site.register(Service)
admin.site.register(Testimony)
admin.site.register(Status)
admin.site.register(LaundryList)
admin.site.register(Item)