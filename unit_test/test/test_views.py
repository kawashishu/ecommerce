import datetime
from django.test import RequestFactory, TestCase, Client
from django.urls import reverse

from store.models import Product, Coupon, Order, OrderItem, ProductImage, Category
from customer.models import Customer
from checkout.models import BillingAddress
from checkout.views.checkout import CheckoutView
from unit_test.test.factories import CustomerFactory, BillingAddressFactory, ProductFactory, CouponFactory
from django.contrib.sessions.middleware import SessionMiddleware

class CheckoutViewTest(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.user = CustomerFactory()
        self.product = ProductFactory()
        self.default_billing_address = BillingAddressFactory(email=self.user, default=True)
        self.billing_address = BillingAddressFactory(email=self.user, default=False)
        self.coupon = CouponFactory(customer=self.user, expiration_date=datetime.datetime.now() + datetime.timedelta(days=30), is_use=False)
        self.use_coupon = CouponFactory(customer=self.user, expiration_date=datetime.datetime.now() + datetime.timedelta(days=30), is_use=True)
    
    def test_get_with_coupon(self):
        request = self.factory.get('checkout')
        request.user = self.user
        request.session = {'shipping_fee': 10, 'coupon_id': self.coupon.id}
        view = CheckoutView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['use_coupon'], self.coupon)
        self.assertEqual(response.context_data['default_billing_address'], self.default_billing_address)
        self.assertEqual(response.context_data['billing_address'], self.billing_address)
        self.assertEqual(response.context_data['coupons'], [self.coupon])
        self.assertEqual(response.context_data['shipping'], 10)
    
    def test_post_with_valid_data(self):
        request = self.factory.post(reverse('checkout'), {'order-note': 'Test note', 'use_coupon_id': self.coupon.id, 'sumtotal': '100.00'})
        request.user = self.user
        request.session = {'cart-duplicate': [self.product.id]}
        response = self.view(request)
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dash-order'))
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderItem.objects.count(), 1)
        self.assertEqual(OrderItem.objects.first().product, self.product)
        self.assertEqual(OrderItem.objects.first().quantity, 1)
        self.assertEqual(OrderItem.objects.first().price, self.product.price)
        self.assertEqual(self.coupon.is_use, True)
        self.assertEqual(request.session['cart'], [])
        self.assertEqual(request.session['cart-duplicate'], [])
        self.assertEqual(request.session['coupon_id'], None)

class SetFalseDefaultBillingAddressTest(TestCase):
    def setUp(self):
        self.user = CustomerFactory()
        self.default_billing_address = BillingAddressFactory(email=self.user, default=True)
        self.non_default_billing_address = BillingAddressFactory(email=self.user, default=False)

    def test_set_false_default_billing_address(self):
        # Test with a user that has a default billing address
        self.client.force_login(self.user)
        response = self.client.get(reverse('set_false_default_billing_address'))
        self.assertEqual(response.status_code, 200)
        self.default_billing_address.refresh_from_db()
        self.assertFalse(self.default_billing_address.default)

        
    def test_set_false_default_billing_address_no_default(self):
        # Test with a user that doesn't have a default billing address
        self.default_billing_address.delete()
        self.client.force_login(self.user)
        response = self.client.get(reverse('set_false_default_billing_address'))
        self.assertEqual(response.status_code, 400)

