from django.contrib import admin
from .models import Item, Category

# Register your models here.

class ItemsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")

admin.site.register(Item, ItemsAdmin)
admin.site.register(Category)
