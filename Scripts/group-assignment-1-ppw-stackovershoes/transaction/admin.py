from django.contrib import admin
from .models import Transaction

# Register your models here.

class TransAdmin(admin.ModelAdmin):
    list_display = ("buyer", "item", "date")

admin.site.register(Transaction, TransAdmin)