from django.db import models

# Create your models here.


class Voucher(models.Model):
    code_name     = models.CharField(max_length=20, primary_key=True)
    price_cut     = models.PositiveSmallIntegerField()
    minimum_price = models.IntegerField()
    expired_date  = models.DateField()

    def __str__(self):
        return self.code_name


