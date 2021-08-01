from django.contrib import admin
from .models import Voucher

# Register your models here.

class VoucherAdmin(admin.ModelAdmin):
    list_display = ("code_name", "price_cut", "expired_date")

admin.site.register(Voucher, VoucherAdmin)