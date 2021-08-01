from django.db import models
# Create your models here.

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)



class Review(models.Model):
    reviewer_name = models.CharField(max_length=20)  
    rev_title     = models.CharField(max_length=50)
    message       = models.TextField()
    date_created  = models.DateTimeField(auto_now_add=True)
    rating        = IntegerRangeField(min_value=1, max_value=5, default='5')
    
    def __str__(self):
        return self.reviewer_name