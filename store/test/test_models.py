from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from store.models import Product, Order, Category
from customer.models import Customer

from checkout.models import BillingAddress


class TestModelCategory(TestCase):
    def setUp(self):
        category = Category.objects.create(
            name='testCategory',
            image='testImage',
        )
        self.Product = Product.objects.create(
            name='testName',
            decripstion='testDescription',
            quanlity=1,
            discount=1,
            status=True,
            title='testTitle',
            price=1,
            views=1,
            avatar='testAvatar',
            categoryid=category,
        )

    def test_product(self):
        self.assertEqual(self.Product.name, 'testName')
        self.assertEqual(self.Product.decripstion, 'testDescription')
        self.assertEqual(self.Product.quanlity, 1)
        self.assertEqual(self.Product.discount, 1)
        self.assertEqual(self.Product.status, True)
        self.assertEqual(self.Product.title, 'testTitle')
        self.assertEqual(self.Product.price, 1)
        self.assertEqual(self.Product.views, 1)
        self.assertEqual(self.Product.avatar, 'testAvatar')
        self.assertEqual(self.Product.categoryid, Category.objects.get(id=1))

class TestModelOrder(TestCase):
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