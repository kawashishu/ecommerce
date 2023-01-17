from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from decimal import Decimal
from datetime import datetime
from store.models import Product, Order, OrderItem, BillingAddress, Coupon

class CheckoutViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='testuser@example.com', password='testpassword')
        self.product = Product.objects.create(
            name='Test Product', price=Decimal('10.00'), quantity=10)
        self.coupon = Coupon.objects.create(
            code='TEST', expiration_date=datetime.now())
        self.billing_address = BillingAddress.objects.create(
            email=self.user, default=True)

    def test_view_uses_correct_template(self):
        request = self.factory.get(reverse('checkout'))
        request.user = self.user
        request.session = {'shipping_fee': 10, 'coupon_id': self.coupon.id}
        view = CheckoutView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')

    def test_view_calculates_correct_total(self):
        request = self.factory.get(reverse('checkout'))
        request.user = self.user
        request.session = {'shipping_fee': 10, 'coupon_id': self.coupon.id, 'cart': [self.product.id]}
        view = CheckoutView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['total'], 10)
        self.assertEqual(response.context_data['sumtotal'], 20)

    def test_view_handles_product_stock(self):
        request = self.factory.post(reverse('checkout'))
        request.user = self.user
        request.session = {
            'shipping_fee': 10, 'coupon_id': self.coupon.id,
            'cart': [self.product.id], 'cart-duplicate': [self.product.id, self.product.id]
        }
        request.POST = {
            'order-note': 'Test note',
            'use_coupon_id': self.coupon.id,
            'sumtotal': '20,00'
        }
        view = CheckoutView.as_view()
        response = view(request)
        self.assertRedirects(response, reverse('checkout'), target_status_code=400)
        self.assertEqual(Order.objects.count(), 0)
        self.assertEqual(OrderItem.objects.count(), 0)
        self.assertEqual(self.product.quantity, 10)

    def test_view_redirects_if_not_authenticated(self):
        request = self.factory.get(reverse('checkout'))
        request.session = {'shipping_fee': 10, 'coupon_id': self.coupon.id}
        view = CheckoutView.as_view()
        response = view(request)
        self.assertRedirects(response, '/accounts/login/?next=' + reverse('checkout'))

from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
 
class BillingAddressTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory() 
        self.user = User.objects.create_user(
            username='testuser', email='testuser@example.com', password='testpassword')
        self.billing_address = BillingAddress.objects.create(
            email=self.user, default=True, shipping_fee=10)

    def test_set_false_default_billing_address(self):
        request = self.factory.get(reverse('create_billing_address'))
        request.user = self.user
        response = set_false_default_billing_address(request)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(BillingAddress.objects.filter(default=True).exists())

    def test_set_default_billing_address(self):
        request = self.factory.post(reverse('set_default_billing_address'))
        request.user = self.user
        request.POST = {'default-address': self.billing_address.id}
        response = set_default_billing_address(request)
        self.assertRedirects(response, reverse('checkout'))
        self.assertTrue(BillingAddress.objects.get(id=self.billing_address.id).default)
        self.assertEqual(request.session['shipping_fee'], 10)

    def test_create_billing_address(self):
        request = self.factory.post(reverse('create_billing_address'))
        request.user = self.user
        request.POST = {
            'shipping_fee': 10,
            'province': 'Test Province',
            'district': 'Test District',
            'ward': 'Test Ward',
            'street_address': 'Test Street Address',
            'mobilephone': '1234567890'
        }
        response = create_billing_address(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(BillingAddress.objects.count(), 2)
        self.assertTrue(BillingAddress.objects.filter(default=True).exists())
        self.assertEqual(request.session['shipping_fee'], 10)

    def test_create_billing_address_with_get_request(self):
        request = self.factory.get(reverse('create_billing_address'))
        request.user = self.user
        response = create_billing_address(request)
        self.assertEqual(response.status_code, 400)
