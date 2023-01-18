from datetime import timezone
from factory import Faker, SubFactory, Sequence, Iterator

from factory.django import DjangoModelFactory
from django.test import TestCase
from customer.models import Customer, SEX_CHOICES
from checkout.models import BillingAddress
from store.models import Category, Product, ProductImage,Coupon, Notification, Order, OrderItem
from comment.models import Comment

class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer

    name = Faker('name')
    email = Faker('email')
    password = Faker('password')
    phone = Faker('phone_number')
    address = Faker('address')
    status = Faker('random_element', elements=[True, False])
    avatar = 'images_customer/default.png'
    age = Faker('random_int', min=0, max=100)
    sex = Sequence(lambda n: SEX_CHOICES[n % len(SEX_CHOICES)][0])


class BillingAddressFactory(DjangoModelFactory):
    class Meta:
        model = BillingAddress

    email = SubFactory(CustomerFactory)
    name = Faker('name')
    province = Faker('state')
    district = Faker('city')
    ward = Faker('street_name')
    street_address = Faker('street_address')
    mobilephone = Faker('phone_number')
    default = Faker('random_element', elements=[True, False])
    shipping_fee = Faker('random_int', min=0, max=100)

class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = Faker('word')
    image = Faker('image_url', width=800, height=800)
    description = Faker('paragraph')

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = Faker('name')
    category = SubFactory(CategoryFactory)
    decripstion = Faker('paragraph')
    quantity = Faker('random_int', min=0, max=1000)
    discount = Faker('random_int', min=0, max=50)
    status = Faker('random_element', elements=[True, False])
    title = Faker('sentence', nb_words=4)
    price = Faker('random_int', min=0, max=1000)
    avatar = Faker('image_url', width=800, height=800)
    rating = Faker('random_int', min=1, max=5)

class NotificationFactory(DjangoModelFactory):
    class Meta:
        model = Notification

    content = Faker('sentence', nb_words=4)
    customer = SubFactory(CustomerFactory)
    read = Faker('random_element', elements=[True, False])
    link = Faker('random_element', elements=Notification.LINK_CHOICES)

class CouponFactory(DjangoModelFactory):
    class Meta:
        model = Coupon

    code = Faker('pystr', max_chars=10)
    expiration_date = Faker('date_between', start_date='+1d', end_date='+30d')
    discount_amount = Faker('random_int', min=0, max=100)
    customer = SubFactory(CustomerFactory)
    is_use = Faker('random_element', elements=[True, False])
    image = Faker('image_url', width=800, height=800)
    decription = Faker('paragraph')

class OrderFactory(DjangoModelFactory):

    class Meta:
        model = Order

    created = Faker('date_time_this_decade', tzinfo=timezone.utc)
    name = Faker('name')
    total = Faker('pyfloat', left_digits=3, right_digits=2, positive=True)
    status = Faker('random_element', elements=[True, False])
    customer = SubFactory(CustomerFactory)
    billing_address = SubFactory(BillingAddressFactory)
    note = Faker('paragraph')
    state = Faker('random_element', elements=[x[0] for x in Order.ORDER_STATUS_CHOICES])
    total_shipping_fee = Faker('pyfloat', left_digits=3, right_digits=2, positive=True)
    coupon = SubFactory(CouponFactory)

class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    content = Faker('text')
    customer = SubFactory(CustomerFactory)
    product = SubFactory(ProductFactory)
    rating = Faker('random_int', min=1, max=5)