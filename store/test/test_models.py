from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from store.models import Product, Order, Category
from customer.models import Customer

from checkout.models import BillingAddress

from store.test.factories import ProductFactory, CategoryFactory, OrderFactory, OrderDetailFactory
from customer.test.factory import CustomerFactory
from checkout.test.factory import BillingAddressFactory

from faker import Faker

fake = Faker()
class TestModelCategory(TestCase):
    def setUp(self):
        name = fake.name()
        self.category = CategoryFactory(name=name, image=f'image_{name}')
    
    def test_category_model(self):
        self.assertEqual(self.category.name, self.category.name)
        self.assertEqual(self.category.image, self.category.image)
    
class TestModelProduct(TestCase):
    def setUp(self):
        name = fake.name()
        self.product = ProductFactory(name=name, avatar=f'image_{name}')
    
    def test_product_model(self):
        self.assertEqual(self.product.name, self.product.name)
        self.assertEqual(self.product.avatar, self.product.avatar)
        
class TestModelOrder(TestCase):
    def setUp(self):
        self.customer = CustomerFactory()
        self.customer = BillingAddressFactory()
        self.order = OrderFactory()
    
    def test_order_model(self):
        self.assertEqual(self.order.created, self.order.created)
        self.assertEqual(self.order.status, self.order.status)
        