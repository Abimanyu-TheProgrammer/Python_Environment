from django import forms
from homepage.models import Item
from .models import Transaction
from Voucher.models import Voucher

class AddTransaction(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = {
            'buyer',
            'item',
            'voucher',
            'total_price'
        }

    item_id = forms.CharField(max_length=6)
    voucher_name = forms.CharField(max_length=20)

    def __init__(self, *args, **kwargs):
        super(AddTransaction, self).__init__(*args, **kwargs)
        self.fields['item'].required = False
        self.fields['voucher'].required = False
        self.fields['total_price'].required = False

    def clean(self):
        item = self.cleaned_data.get('item_id')
        if not item:
            raise forms.ValidationError("Item does not exist!")
        
        item = Items.objects.get(id=item)
        self.cleaned_data['total_price'] = item.price

        self.cleaned_data['voucher'] = None
        voucher = self.cleaned_data.get('voucher_name')
        if voucher:
            voucher = Voucher.objects.get(code_name=voucher)
            self.cleaned_data['voucher'] = voucher
            self.cleaned_data['total_price'] = (item.price*voucher.price_cut)//100

        return super(AddTransaction, self).clean()