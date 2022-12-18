from django import forms
from .models import Customer
from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import UserChangeForm


class RegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'input-text input-text--primary-style',
        'placeholder': 'Enter your name',
    }))

    phone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'input-text input-text--primary-style',
        'placeholder': 'Enter phone number',
    }))

    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={
         'class': 'input-text input-text--primary-style', 
         'placeholder': 'Enter email',
    }))

    captcha = ReCaptchaField()

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-text input-text--primary-style',
        'placeholder': 'Enter password',
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password',
        'class': 'input-text input-text--primary-style',
    }))

    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'password', 'confirm_password', 'captcha']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
    
        if password != confirm_password:
            raise forms.ValidationError(
                'Password does not match!'
            )

SEX_CHOICES = {
    ('W', 'Women'),
    ('M', 'Man'),
}

    
class UpdateProfileForm(UserChangeForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'enter name',
    }))
    
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'enter phone',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'enter address',
    }))
    
    avatar = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control', 
        }),required=False)
    
    password = None
    class Meta:
        model= Customer
        fields = ['name', 'phone', 'address', 'avatar','age', 'sex']