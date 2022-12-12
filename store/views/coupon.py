from django.shortcuts import redirect, render
from django.views.generic import FormView
from django.urls import reverse_lazy
from store.forms import CouponForm
from store.models import Coupon


class ApplyCouponView(FormView):
    template_name = 'checkout.html'
    form_class = CouponForm
    success_url = reverse_lazy('checkout')

    def form_valid(self, form):
        code = form.cleaned_data.get('code')
        
        

        return super().form_valid(form)