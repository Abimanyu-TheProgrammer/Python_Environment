from django import forms
import datetime
from .models import DpayTopUpTransaction, Testimony, Service, LaundryList,Item
from django.db import connection, transaction

class TopUp_Input(forms.ModelForm):
    class Meta:
        model = DpayTopUpTransaction
        fields = ('email', 'nominal')

class TopUp_Update(forms.ModelForm):
    class Meta:
        model = DpayTopUpTransaction
        fields = (
            'nominal',
        )

class TestimonyForm(forms.Form):
    emailList=[]
    trasaction_dateList=[]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     with connection.cursor() as cursor:
    #         cursor.execute("SELECT email FROM laundry_transaction")
    #         self.fields['id_produk'].choices = cursor.fetchall()
    #         cursor.execute("SELECT transaction_date FROM laundry_transaction where email =")
    #         self.fields['id_apotek'].choices = cursor.fetchall()

# email and transaction_date are supposed to be choicefiels
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-control'})) 
    transaction_date = forms.DateTimeField(widget = forms.DateTimeInput(attrs= {'type':'text', 'placeholder':'2019-04-27 17:20:20', 'class':'form-control'}))
    testimony_date = forms.DateTimeField(widget = forms.DateTimeInput(attrs= {'type':'text', 'placeholder':'2019-04-27 17:20:20', 'class':'form-control'}))
    status = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

class Testimony_Update(forms.Form):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'readonly':True,'class':'form-control'})) 
    transaction_date = forms.DateTimeField(widget = forms.DateInput(attrs= {'readonly':True, 'class':'form-control'}))
    status = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    def save(self):
        try:
            with connection.cursor() as cursor:
                with transaction.atomic():
                    cursor.execute("""\
                    UPDATE TESTIMONY SET status = %s, rating = %s
                    WHERE email=%s AND transaction_date=%s""",
                                   [cleaned.get("status"), cleaned.get("rating"),
                                   cleaned.get('email'), cleaned.get('transaction_date')])
        except IntegrityError:
            pass


class newTestimony(TestimonyForm):

    def save(self):
        cleaned = self.cleaned_data
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO TESTIMONY VALUES(%s, %s, %s, %s, %s)",
                           [cleaned.get("email"), cleaned.get("trasaction_date"),
                            cleaned.get("testimony_date"), cleaned.get("status"),
                            cleaned.get("rating")
                            ])


class ServiceForm(forms.Form):

    code = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':True}),
        max_length=20)
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50)
    duration = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'In Minutes'}),
        max_length=10)
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}),
        decimal_places = 2, max_digits = 9)

class LaundryList_Update(forms.ModelForm):
    class Meta:
        model = LaundryList
        fields = ('serialno', 'amount','itemtype')

class LaundryListForm(forms.ModelForm):
    class Meta:
        model = LaundryList
        fields = '__all__'

class ItemForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean(self):
        old_code = self.cleaned_data.get('code')
        new_code = self.cleaned_data.get('code')

        with connection.cursor() as cursor:
            cursor.execute("SELECT code FROM ITEM "
                           "WHERE code!=%s", [old_code])
            existing_data = cursor.fetchall()

        if (new_code) in existing_data:
            raise forms.ValidationError("Code %s already exists Apotek %s", [old_code])

    def save(self):
        cleaned = self.cleaned_data
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO ITEM VALUES(%s, %s)",
                           [cleaned.get("code"), cleaned.get("name")])

class CustomerForm(forms.Form):
    gender_choices=[
	('m', 'Male'),
	('f', 'Female'),
	]

    email = forms.EmailField(widget = forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}), max_length = 20)
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=20)
    phonenumber = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 10)
    gender = forms.CharField(label=("Jenis Kelamin"), required=True, widget=forms.Select(choices=gender_choices))
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'placeholder':'2019-04-27'}))

class StaffForm(forms.Form):
    gender_choices=[
	('m', 'Male'),
	('f', 'Female'),
	]

    email = forms.EmailField(widget = forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}), max_length = 20)
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=20)
    phonenumber = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 10)
    gender = forms.CharField(label=("Jenis Kelamin"), required=True, widget=forms.Select(choices=gender_choices))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 50)
    npwp = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 20)
    account_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 10)
    bank = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 10)
    branch_office = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 10)
    
class CourierForm(forms.Form):
    gender_choices=[
	('m', 'Male'),
	('f', 'Female'),
	]


    email = forms.EmailField(widget = forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}), max_length = 20)
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=20)
    phonenumber = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 10)
    gender = forms.CharField(label=("Jenis Kelamin"), required=True, widget=forms.Select(choices=gender_choices))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 50)
    npwp = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 20)
    account_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 10)
    bank = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 10)
    branch_office = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 10)
    sim_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 10)
    vehicle_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 10)
    vehicle_type = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 10)

class loginForm(forms.Form):
    email = forms.CharField(label=("Email"), required=True, max_length=50)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput(), required=True, max_length=128)