from django import forms


class CouponForm(forms.Form):
    code = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control border-0 p-4',
        'placeholder': 'Coupon code',
        }))
