from django.db import models
from django.conf import settings

# https://stackoverflow.com/questions/44313667/django-using-instance-id-while-uploading-image
def get_image_path(instance, filename):
    return "img/items/{id}/{file}".format(root=settings.MEDIA_URL, id=str(instance.id), file=filename)

# Create your models here.
class Item(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(max_length=100)
    img_url = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    # img_url = models.ImageField(upload_to="img/items/")

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_image = self.image
            self.image = None

            super(Item, self).save(*args, **kwargs)

            self.image = saved_image
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super(Item, self).save(*args, **kwargs)
    
    def __str__(self):
        return "{} {}, {}".format(self.id, str(self.category), self.name)

class Category(models.Model):
    name = models.CharField(max_length=15, primary_key=True)

    def __str__(self):
        return self.name