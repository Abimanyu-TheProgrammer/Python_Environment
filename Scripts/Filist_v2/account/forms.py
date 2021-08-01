from django import forms
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField


Account_Type_Choices = [
    ("R","Roaster"),
    ("C", "Coffee Shop"),
    ("F", "Farmer")
]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = PhoneNumberField(help_text="eg. +62123456789")
    bank_account_number = forms.CharField(max_length = 20)
    location = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SellerRegisterForm(forms.Form):
    company_name = forms.CharField(max_length=50)
    location = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    account_type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=Account_Type_Choices)


    