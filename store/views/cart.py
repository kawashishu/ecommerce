
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from store.models import Product
from django.views.generic import ListView
from store.models import Coupon

SHIPPING_CHARGE = 8


class CartView(View):

    def get(self, request):
        carts = request.session.get('cart-duplicate')
        shipping_fee = request.session.get('shipping_fee') or 0
        print(shipping_fee, "shipping_fee")
        total = 0
        coupon = request.session.get('coupon_id')
        if coupon:
            coupon = Coupon.objects.get(id=coupon)
        list_coupons = Coupon.objects.filter(customer=request.user)
        try:
            quantity = {i: carts.count(i) for i in carts}
            products = Product.objects.filter(id__in=carts)
            for product in products:
                total += product.price * quantity[product.id]

            context = {
                'products': products,
                'total': int(total),
                'SumTotal': int(total + shipping_fee),
                'quantity': quantity,
                'shipping': shipping_fee,
                'list_coupons': list_coupons,
                'coupon': coupon,
            }
        except TypeError:
            context = {
                'total': 0,
                'shipping': shipping_fee,
            }
        return render(request, 'cart.html', context)

    def post(self, request):
        id = int(request.POST.get('id'))
        if 'cart' in request.session:
            if id in request.session['cart']:
                request.session['cart-duplicate'].insert(0, id)
                print(request.session['cart-duplicate'], "duplicate")
            else:
                request.session['cart'].insert(0, id)
                request.session['cart-duplicate'].insert(0, id)
                print(request.session['cart-duplicate'], "None_duplicate")
        else:
            request.session['cart'] = [id]
            request.session['cart-duplicate'] = [id]
            print(request.session['cart-duplicate'])
        request.session.modified = True
        return HttpResponse(len(request.session['cart-duplicate']))


class CartListView(ListView):
    def post(self, request):
        id = int(request.POST.get('id'))
        remove(request, id)
        total = getTotal(request)
        count = len(request.session.get('cart-duplicate') or [])
        return JsonResponse({'total': total, 'count': count}, )


def remove(request, id):
    try:
        request.session['cart'].remove(id)
        while id in request.session['cart-duplicate']:
            request.session['cart-duplicate'].remove(id)
        request.session.modified = True
    except ValueError:
        return False
    return True


def getTotal(request):
    try:
        carts = request.session['cart-duplicate']
        quanlity = {i: carts.count(i) for i in carts}
        products = Product.objects.filter(id__in=carts)
        total = 0
        for product in products:
            total += product.price * quanlity[product.id]
        return total
    except TypeError:
        return 0


def getQuanlity(request):
    try:
        carts = request.session['cart-duplicate']
        quanlity = {i: carts.count(i) for i in carts}
        return quanlity
    except TypeError:
        return 0

# get cart


def getCart(request):
    try:
        carts = request.session['cart-duplicate']
        products = Product.objects.filter(id__in=carts)
        return products
    except TypeError:
        return 0


class WishListView(View):
    def get(self, request):

        wishlist = request.session.get('wishlist') or []
        products = Product.objects.filter(id__in=wishlist)
        context = {
            'products': products,
        }
        return render(request, 'wishlist.html', context)

    def post(self, request):
        id = int(request.POST.get('id'))
        if 'wishlist' in request.session:
            if id in request.session['wishlist']:
                request.session['wishlist'].remove(id)
            else:
                request.session['wishlist'].insert(0, id)
        else:
            request.session['wishlist'] = [id]
        request.session.modified = True
        return HttpResponse(len(request.session['wishlist']))


class RemoveWishListView(View):
    def post(self, request):
        id = int(request.POST.get('id'))
        try:
            request.session['wishlist'].remove(id)
            request.session.modified = True
        except ValueError:
            return False
        return HttpResponse(len(request.session.get('wishlist') or []))


class CartCalculator(View):
    def post(self, request):
        id = int(request.POST.get('id'))
        btn = request.POST.get('btn')
        if btn == 'fa-plus':
            request.session['cart-duplicate'].insert(0, id)
        elif btn == 'fa-minus':
            request.session['cart-duplicate'].remove(id)
        request.session.modified = True
        carts = request.session.get('cart-duplicate')
        total = 0
        try:
            quanlity = {i: carts.count(i) for i in carts}
            products = Product.objects.filter(id__in=carts)
            for product in products:
                total += product.price * quanlity[product.id]
        except TypeError:
            total = 0
        total *= request.session.get('currency') or 1
        return HttpResponse(total)
