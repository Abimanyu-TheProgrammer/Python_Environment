from django import forms
from .models import Product

class TestForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'