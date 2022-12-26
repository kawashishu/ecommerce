
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from checkout.forms import BillingAddressForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from checkout.models import BillingAddress
from store.models import Order
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from store.views.cart import getTotal
from store.models import Product


class CheckoutView(View):
    @method_decorator(login_required, name='dispatch')
    def get(self, *args, **kwargs):
        shipping_fee = self.request.session.get('shipping_fee') or 0
        form = BillingAddressForm()
        total = getTotal(self.request)
        context = {
            'form': form,
            'total': int(total),
            'sumtotal': int(total) + shipping_fee,
            'shipping': shipping_fee,
            'default_billing_address': BillingAddress.objects.filter(
                email=self.request.user, default=True).first(),
            'billing_address': BillingAddress.objects.filter(
                email=self.request.user)
        }
        return render(self.request, "checkout.html", context)

    def post(self, *args, **kwargs):
        try:
            note = self.request.POST.get('order-note')
            print(self.request.POST)
            billing_address = BillingAddress.objects.get(
                email=self.request.user, default=True)
            order = Order(
                billing_address=billing_address,
                state=Order.PROCESS,
                customer=self.request.user,
                note=note,
                total=getTotal(self.request)

            )
            billing_address.save()
            order.save()
            if process_order(self.request):
                self.request.session['cart'] = []
                self.request.session['cart-duplicate'] = []
            messages.success(self.request, "Order successfully")
            return redirect("dash-order")
        except ObjectDoesNotExist:
            print("You do not have an active order")
            messages.error(self.request, "You do not have an active order")
            return redirect("dash-order")


def process_order(request):
    if request.user.is_authenticated:
        try:
            carts = request.session.get('cart-duplicate')
            quantity = {i: carts.count(i) for i in carts}
            products = Product.objects.filter(id__in=carts)
            for product in products:
                if product.quantity > quantity[product.id]:
                    product.quantity -= quantity[product.id]
                    product.save()
                else:
                    messages.error(request,
                                   f"Product {product.name} is out of stock")
                    return False
        except Exception as e:
            messages.error(request, e)
            return False
    return True


def save_billing_address(request):
    form = BillingAddressForm(request.POST or None)
    if request.user.is_authenticated:
        try:
            if form.is_valid():
                print("Form is valid")
                name = form.cleaned_data.get('name')
                mobilephone = form.cleaned_data.get('mobilephone')
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                country = form.cleaned_data.get('country')

                billing_address = BillingAddress(
                    email=request.user,
                    name=name,
                    street_address=street_address,
                    apartment_address=apartment_address,
                    countries=country,
                    mobilephone=mobilephone
                )
                billing_address.save()
            else:
                return redirect("checkout")
        except Exception as e:
            messages.error(request, e)
            return redirect("checkout")
    return redirect("checkout")


def set_default_billing_address(request):
    if request.method == 'POST':
        default_billing_address = BillingAddress.objects.get(
            email=request.user, default=True)
        if default_billing_address:
            default_billing_address.default = False
            default_billing_address.save()

        billing_address_id = request.POST.get('default-address')
        billing_address = BillingAddress.objects.get(id=billing_address_id)
        billing_address.default = True
        billing_address.save()

        return redirect("checkout")
    else:
        messages.error(request, "Something error, try it again")
        return redirect("checkout")


def set_shipping_fee(request):
    shipping_fee = int(request.POST.get('shipping_fee'))
    if request.method == 'POST':
        request.session['shipping_fee'] = shipping_fee
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)
