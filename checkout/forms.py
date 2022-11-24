from django import forms
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = {
    ('P', 'Paypal'),
    ('M', 'Momo'),
}

class CheckoutForm(forms.Form):

    mobilephone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Mobile Phone','class': 'form-control'}))

    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your address', 'class': 'form-control' }))

    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Apartment or suite', 'class': 'form-control' }))

    country = CountryField(blank_label='select country').formfield(
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))

    zip = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control' }))

    same_billing_address = forms.BooleanField(required=False ,widget=forms.CheckboxInput())
    
    save_info = forms.BooleanField(required=False ,widget=forms.CheckboxInput(
        attrs={'class': 'custom-control-input', 'id': 'newaccount'}))

    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES, required = False)


