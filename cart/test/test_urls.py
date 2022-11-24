from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cart.views.views import CartView, CartListView, remove, getTotal, getQuanlity, getCart

class TestUrls(SimpleTestCase):

    def test_cart_url_is_resolved(self):
        url = reverse('cart')
        self.assertEquals(resolve(url).func.view_class, CartView)

    def test_cart_list_url_is_resolved(self):
        url = reverse('cart-list')
        self.assertEquals(resolve(url).func.view_class, CartListView)

    
    
    