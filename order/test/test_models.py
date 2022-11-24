from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from checkout.models import BillingAddress
from order.models import Order
from customer.models import Customer

class TestModel(TestCase):
    def setUp(self):
        customer = Customer.objects.create(
            name = 'Nguye',
            email = 'test@gmail.com',
            phone = '01234',
        )
        billing_address = BillingAddress.objects.create(
            street_address = 'test',
            apartment_address = 'test',
            email = customer,
            mobilephone='01234',
        )
        self.Order = Order.objects.create(
            email = 'test@gmail.com',
            state = 0,
            billing_address = billing_address,
            customerid = customer,
            status = True,
        )
    def test_order(self):
        self.assertEqual(self.Order.email, 'test@gmail.com')
        self.assertEqual(self.Order.billing_address, BillingAddress.objects.get(id=1))
        self.assertAlmostEqual(self.Order.customerid, Customer.objects.get(id=1))