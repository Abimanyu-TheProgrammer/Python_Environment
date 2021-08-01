from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    images = models.ImageField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name

@receiver(post_delete, sender=Product)
def submission_delete(sender, instance, **kwargs):
    instance.images.delete(False) 