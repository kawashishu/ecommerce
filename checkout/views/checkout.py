
from django.shortcuts import redirect, render
from django.views import View
from checkout.forms import CheckoutForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from checkout.models import BillingAddress
from store.models import Order
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from store.views.cart import getTotal

SHIPPING_CHARGE = 10

class CheckoutView(View):
    @method_decorator(login_required, name='dispatch')
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        total = getTotal(self.request)
        context = {
            'form': form,
            'total': int(total),
            'sumtotal': int(total) + SHIPPING_CHARGE,
            'shipping': SHIPPING_CHARGE,
        }
        return render(self.request, "checkout.html", context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            if form.is_valid():
                mobilephone = form.cleaned_data.get('mobilephone')
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                country = form.cleaned_data.get('country')

                billing_address = BillingAddress(
                    email=self.request.user,
                    street_address=street_address,
                    apartment_address=apartment_address,
                    countries=country,
                    mobilephone=mobilephone
                )
                order = Order(
                    billing_address=billing_address,
                    state = 1,
                    customer=self.request.user,
                )
                billing_address.save()
                order.save()
                return redirect("billing")
        except ObjectDoesNotExist:
                messages.error(self.request, "You do not have an active order")
                return redirect("billing")
