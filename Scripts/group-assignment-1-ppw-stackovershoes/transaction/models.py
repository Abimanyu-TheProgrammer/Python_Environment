from django.db import models

# Create your models here.

class Transaction(models.Model):
    buyer = models.CharField(max_length=50)
    item = models.ForeignKey('homepage.Item', on_delete=models.CASCADE)
    voucher = models.ForeignKey('Voucher.Voucher', on_delete=models.CASCADE, blank=True, null=True)
    total_price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}: {}".format(self.buyer, str(self.item))