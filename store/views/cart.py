
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from store.models import Product
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

SHIPPING_CHARGE = 8

class CartView(View):
    def get(self, request):
        carts = request.session.get('cart-duplicate')
        total = 0
        try:
            quanlity = {i: carts.count(i) for i in carts}
            products = Product.objects.filter(id__in=carts)
            for product in products:
                total += product.price * quanlity[product.id]

            context = {
                'products': products,
                'total': total,
                'SumTotal': total + SHIPPING_CHARGE,
                'quanlity': quanlity,
            }
        except:
            context = {}

        return render(request, 'cart.html', context)

    def post(self, request):
        id = int(request.POST.get('id'))
        if 'cart' in request.session:
            if id in request.session['cart']:
                request.session['cart-duplicate'].insert(0, id)
            else:
                request.session['cart'].insert(0, id)
                request.session['cart-duplicate'].insert(0, id)
        else:
            request.session['cart'] = [id]
            request.session['cart-duplicate'] = [id]
        request.session.modified = True
        return HttpResponse(len(request.session['cart-duplicate']))


class CartListView(ListView):
    def post(self, request):
        id = int(request.POST.get('id'))
        remove(request, id)
        total = getTotal(request)
        return HttpResponse(total)


def remove(request, id):
    try:
        request.session['cart'].remove(id)
        while id in request.session['cart-duplicate']:
            request.session['cart-duplicate'].remove(id)
        request.session.modified = True
    except:
        return HttpResponse("error")
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
    except:
        return 0

# get quanlity


def getQuanlity(request):
    try:
        carts = request.session['cart-duplicate']
        quanlity = {i: carts.count(i) for i in carts}
        return quanlity
    except:
        return 1

# get cart


def getCart(request):
    try:
        carts = request.session['cart-duplicate']
        products = Product.objects.filter(id__in=carts)
        return products
    except:
        return 0

class WishlistView(View):
    @login_required(login_url='register')
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


class CartCalculator(View):
    def post(self, request):
        id = int(request.POST.get('id'))
        btn = request.POST.get('btn')
        if btn == 'fa fa-plus':
            request.session['cart-duplicate'].insert(0, id)
        elif btn == 'fa fa-minus':
            request.session['cart-duplicate'].remove(id)
        request.session.modified = True
        carts = request.session.get('cart-duplicate')
        total = 0
        try:
            quanlity = {i: carts.count(i) for i in carts}
            products = Product.objects.filter(id__in=carts)
            for product in products:
                total += product.price * quanlity[product.id]
        except:
            total = 0
        return HttpResponse(total)

