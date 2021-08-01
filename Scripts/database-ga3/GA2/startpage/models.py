from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class DpayTopUpTransaction(models.Model):
    email = models.EmailField()
    nominal = models.FloatField()
    date = models.DateField(default=timezone.now())

    def __str__(self):
        return str(self.email)


class Status(models.Model):
    code = models.CharField(max_length = 10)
    name = models.CharField(max_length = 15)
    
    def __str__(self):
        return str(self.code)


    def __str__(self):
        return str(self.name)

class Testimony(models.Model):
    email = models.EmailField()
    transaction_date = models.DateField(default=datetime.today())
    status = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return str(self.email)

class Service(models.Model):
    code = models.CharField(max_length= 10)
    name = models.CharField(max_length = 50)
    duration = models.CharField(max_length = 10)
    price = models.DecimalField(decimal_places = 2, max_digits = 9)

    def __str__(self):
        return str(self.code)

class LaundryList(models.Model):
    email = models.EmailField()
    date = models.DateField(default=datetime.today())
    serialno = models.IntegerField()
    amount = models.IntegerField()
    itemtype = models.CharField(max_length = 10)

    def __str__(self):
        return str(self.email)

class Item(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length = 10)

    def __str__(self):
        return str(self.code)