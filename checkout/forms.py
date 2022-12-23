from django import forms
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = {
    ('P', 'Paypal'),
    ('M', 'Momo'),
}

class BillingAddressForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Name Address', 'class': 'input-text input-text--primary-style' }), required=False, max_length=50)

    mobilephone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Mobile Phone','class': 'input-text input-text--primary-style'}))

    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Street Address', 'class': 'input-text input-text--primary-style' }))

    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Apartment or Suite', 'class': 'input-text input-text--primary-style' }))

    country = CountryField(blank_label='Select Country').formfield(
        widget=CountrySelectWidget(attrs={
            'class': 'select-box select-box--primary-style',
        }))


    
    


