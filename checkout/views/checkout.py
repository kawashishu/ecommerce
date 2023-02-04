
import datetime
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from checkout.models import BillingAddress
from store.models import Order
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from store.views.cart import getTotal
from store.models import Product, OrderItem, Coupon
from django.db.models import Q


class CheckoutView(View):
    @method_decorator(login_required, name='dispatch')
    def get(self, *args, **kwargs):

        shipping_fee = self.request.session.get('shipping_fee') or 0
        coupon_use_id = self.request.session.get('coupon_id') or None

        if coupon_use_id:
            use_coupon = Coupon.objects.get(id=coupon_use_id)
        else:
            use_coupon = None

        time = datetime.datetime.now()

        coupons = Coupon.objects.filter(
            customer=self.request.user).filter(Q(expiration_date__gte=time), Q(is_use=False))
        total = getTotal(self.request)

        context = {
            'total': int(total),
            'sumtotal': int(total) + shipping_fee,
            'shipping': shipping_fee,
            'default_billing_address': BillingAddress.objects.filter(
                email=self.request.user, default=True).first(),
            'billing_address': BillingAddress.objects.filter(
                email=self.request.user),
            'coupons': coupons,
            'use_coupon': use_coupon
        }

        return render(self.request, "checkout.html", context)

    def post(self, *args, **kwargs):
        try:
            carts = self.request.session.get('cart-duplicate')
            quantity = {i: carts.count(i) for i in carts}
            products = Product.objects.filter(id__in=carts)

            if check_product_stock(self.request, products, quantity):
                self.request.session['cart'] = []
                self.request.session['cart-duplicate'] = []

                if carts is None:
                    messages.error(self.request, "You do not have an active order")
                    return redirect("checkout")
                note = self.request.POST.get('order-note')
                use_coupon_id = self.request.POST.get('use_coupon_id')
                sumtotal = self.request.POST.get('sumtotal')

                billing_address = BillingAddress.objects.get(
                    email=self.request.user, default=True,
                    )
                if use_coupon_id:
                    coupon = Coupon.objects.get(id=use_coupon_id)
                    coupon.is_use = True
                    coupon.save()
                else:
                    coupon = None
                order = Order(
                    billing_address=billing_address,
                    customer=self.request.user,
                    note=note,
                    total=sumtotal,
                    coupon=coupon,
                )
                self.request.session['coupon_id'] = None
                billing_address.save()
                order.save()

                for product in products:
                    order_item = OrderItem(
                        product=product,
                        quantity=quantity[product.id],
                        price=product.price * quantity[product.id],
                        order=order
                    )

                    order_item.save()

                return redirect("dash-order")
            else:
                return redirect("checkout", status=400)
        except ObjectDoesNotExist:
            return redirect("checkout", status=400)

@transaction.atomic
def check_product_stock(request, products, quantity):
    if request.user.is_authenticated:
        try:
            for product in products:
                if product.quantity > quantity[product.id]:
                    product.quantity -= quantity[product.id]
                    product.save()
                else:
                    return False
        except Exception:
            return False
    return True


def set_false_default_billing_address(request):
    default_billing_address = BillingAddress.objects.filter(
        email=request.user, default=True).first()
        
    if default_billing_address is not None:
        default_billing_address.default = False
        default_billing_address.save()
    else:
        return HttpResponse(status=400)
    return HttpResponse(status=200)


def set_default_billing_address(request):
    if request.method == 'POST':
        set_false_default_billing_address(request)

        billing_address_id = request.POST.get('default-address')
        billing_address = BillingAddress.objects.get(id=billing_address_id)
        billing_address.default = True

        request.session['shipping_fee'] = billing_address.shipping_fee

        billing_address.save()

        return redirect("checkout")
    else:
        messages.error(request, "Something error, try it again")
        return redirect("checkout")


def create_billing_address(request):

    if request.method == 'POST':
        if BillingAddress.objects.exists():
            set_false_default_billing_address(request)

        shipping_fee = int(request.POST.get('shipping_fee'))
        province = request.POST.get('province')
        district = request.POST.get('district')
        ward = request.POST.get('ward')
        street_address = request.POST.get('street_address')
        mobilephone = request.POST.get('mobilephone')

        BillingAddress.objects.create(
            email=request.user,
            province=province,
            district=district,
            ward=ward,
            street_address=street_address,
            mobilephone=mobilephone,
            shipping_fee=shipping_fee,
            default=True
        )

        request.session['shipping_fee'] = shipping_fee
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


