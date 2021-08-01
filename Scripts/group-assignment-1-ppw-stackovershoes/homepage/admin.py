from django.contrib import admin
from .models import Items, Category

# Register your models here.

class ItemsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")

admin.site.register(Items, ItemsAdmin)
admin.site.register(Category)
