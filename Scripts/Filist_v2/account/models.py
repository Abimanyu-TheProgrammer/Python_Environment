from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Products(models.Model):
#     name = models.CharField(max_length=50)
#     desc = models.CharField(max_length=200)
#     price = models.IntegerField()
#     quantity = models.IntegerField()
#     images = models.ImageField()
#     category = models.CharField()

# class Seller(models.Model):
#     user = models.OneToOneField(to= User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     desc = models.CharField(max_length=200)
#     location = models.CharField(max_length=50)
#     product_list = models.ManyToManyField(to=Products)