
from django.test import TestCase
from unit_test.test.factories import CustomerFactory, BillingAddressFactory, \
    CategoryFactory, ProductFactory, NotificationFactory, CouponFactory, \
    OrderFactory, CommentFactory
from comment.models import Comment
from checkout.models import  BillingAddress
from store.models import Category, Product, ProductImage, Coupon, Notification, Order, OrderItem
from faker import Faker
from customer.form import RegistrationForm, UpdateProfileForm

# class RegistrationFormTest(TestCase):
#     def setUp(self):
#         self.customer = CustomerFactory()
#         self.data = {
#             'name': self.customer.name,
#             'phone': self.customer.phone,
#             'email': self.customer.email,
#             'password': self.customer.password,
#             'confirm_password': self.customer.password,
#             'captcha': 'PASSED',
#         }

#     def test_form_valid(self):
#         form = RegistrationForm(data=self.data)
#         self.assertTrue(form.is_valid())

#     def test_form_save(self):
#         form = RegistrationForm(data=self.data)
#         customer = form.save()
#         self.assertEqual(customer.name, self.data['name'])
#         self.assertEqual(customer.phone, self.data['phone'])
#         self.assertEqual(customer.email, self.data['email'])
#         self.assertEqual(customer.password, self.data['password'])
#         self.assertEqual(customer.status, True)
#         self.assertEqual(customer.avatar, 'images_customer/default.png')
#         self.assertEqual(customer.sex, self.customer.sex)
#         self.assertEqual(customer.age, self.customer.age)
    
#     def test_form_invalid(self):
#         form = RegistrationForm(data={})
#         self.assertFalse(form.is_valid())
#         self.assertEqual(form.errors, {
#             'name': ['This field is required.'],
#             'phone': ['This field is required.'],
#             'email': ['This field is required.'],
#             'password': ['This field is required.'],
#             'confirm_password': ['This field is required.'],
#             'captcha': ['This field is required.'],
#         })

class UpdateProfileFormTest(TestCase):
    def setUp(self):
        self.customer = CustomerFactory()
        self.data = {
            'name': self.customer.name,
            'phone': self.customer.phone,
            'address': self.customer.address,
            'avatar': self.customer.avatar,
        }
    def test_form_valid(self):
        form = UpdateProfileForm(data=self.data, instance=self.customer)
        self.assertTrue(form.is_valid())

    def test_form_save(self):
        form = UpdateProfileForm(data=self.data, instance=self.customer)
        customer = form.save()
        self.assertEqual(customer.name, self.data['name'])
        self.assertEqual(customer.phone, self.data['phone'])
        self.assertEqual(customer.address, self.data['address'])
        self.assertEqual(customer.avatar, self.data['avatar'])
    
    def test_form_invalid(self):
        form = UpdateProfileForm(data={}, instance=self.customer)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['This field is required.'],
            'phone': ['This field is required.'],
            'address': ['This field is required.'],
        })
