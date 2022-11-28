
from django.http import HttpResponse
from django.views import View
from cart.views import views
from cart.views.views import SHIPPING_CHARGE
from store.models import Product


class WishlistView(View):
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


class CartView(View):
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
