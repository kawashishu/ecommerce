import datetime
import factory
from django.test import TestCase
from customer.models import Customer, MyCustomerManager ,SEX_CHOICES
from unit_test.test.factories import CustomerFactory, BillingAddressFactory, \
    CategoryFactory, ProductFactory, NotificationFactory, CouponFactory, \
    OrderFactory, CommentFactory
from comment.models import Comment
from checkout.models import  BillingAddress
from store.models import Category, Product, ProductImage, Coupon, Notification, Order, OrderItem
from faker import Faker


class CustomerModelTest(TestCase):
    def test_customer_creation(self):
        customer = CustomerFactory()
        self.assertIsInstance(customer, Customer)
        self.assertEqual(customer.__str__(), customer.email)
        self.assertTrue(customer.is_active)
        self.assertFalse(customer.is_staff)
        

class BillingAddressModelTest(TestCase):
    def test_billing_address_creation(self):
        billing_address = BillingAddressFactory()
        self.assertIsInstance(billing_address, BillingAddress)
        self.assertEqual(billing_address.__str__(), billing_address.province + " " + billing_address.district + " " + str(billing_address.ward) + " " + billing_address.street_address + " " + billing_address.mobilephone)
        self.assertIsNotNone(billing_address.email)
        self.assertTrue(billing_address.email.is_active)

class CategoryTest(TestCase):
    def test_category_creation(self):
        category = CategoryFactory()
        self.assertIsInstance(category, Category)
        self.assertEqual(category.__str__(), category.name)
        self.assertTrue(category.image.url)
        self.assertTrue(category.description)

    def test_to_json(self):
        category = CategoryFactory()
        json_data = category.to_json()
        self.assertEqual(json_data.get('id'), category.id)
        self.assertEqual(json_data.get('name'), category.name)
        self.assertEqual(json_data.get('description'), category.description)

class ProductTest(TestCase):
    def test_product_creation(self):
        product = ProductFactory()
        self.assertIsInstance(product, Product)
        self.assertEqual(product.__str__(), product.name)
        self.assertIsInstance(product.category, Category)
        self.assertTrue(product.decripstion)
        self.assertTrue(product.quantity >= 0)
        self.assertIsInstance(product.status, bool)
        self.assertTrue(product.title)
        self.assertTrue(product.price >= 0)
        self.assertTrue(product.avatar.url)
        self.assertTrue(product.rating >= 1 and product.rating <= 5)

class NotificationTest(TestCase):
    def test_notification_creation(self):
        notification = NotificationFactory()
        self.assertIsInstance(notification, Notification)
        self.assertEqual(notification.__str__(), notification.content)
        self.assertIsInstance(notification.customer, Customer)
        self.assertIsInstance(notification.read, bool)
        self.assertIn(notification.link, Notification.LINK_CHOICES)

class CouponTest(TestCase):
    def test_coupon_creation(self):
        coupon = CouponFactory()
        self.assertIsInstance(coupon, Coupon)
        self.assertEqual(coupon.__str__(), coupon.code)
        self.assertIsInstance(coupon.customer, Customer)
        self.assertIsInstance(coupon.is_use, bool)
        self.assertTrue(coupon.image.url)
        self.assertTrue(coupon.decription)
        self.assertTrue(coupon.discount_amount >= 0 and coupon.discount_amount <= 100)
        self.assertTrue(coupon.expiration_date > datetime.date.today())

class OrderTest(TestCase):
    
    def test_order_creation(self):
        order = OrderFactory()
        self.assertIsInstance(order, Order)
        self.assertIsInstance(order.created, datetime.datetime)
        self.assertTrue(order.name)
        self.assertTrue(order.total >= 0)
        self.assertIs(type(order.status), bool)
        self.assertIsInstance(order.customer, Customer)
        self.assertIsInstance(order.billing_address, BillingAddress)
        self.assertTrue(order.note)
        self.assertTrue(order.total_shipping_fee >= 0)
        self.assertIsInstance(order.coupon, Coupon)
        self.assertEqual(str(order), order.customer.email)



class CommentTestCase(TestCase):
    def setUp(self):
        self.comment = CommentFactory()
    
    def test_comment_creation(self):
        self.assertIsNotNone(self.comment.created)
        self.assertEqual(str(self.comment), self.comment.content)