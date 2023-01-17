from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from store.models import Product
from store.models import Coupon
from django.utils import timezone
from factory import faker
from factory.django import DjangoModelFactory

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = faker.Faker('name')
    price = faker.Faker('random_number', digits=5)
    quantity = faker.Faker('random_number', digits=2)
    image = 'product_image.jpg'
    description = faker.Faker('paragraph')

class CouponFactory(DjangoModelFactory):
    class Meta:
        model = Coupon

    code = faker.Faker('random_number', digits=6)
    expiration_date = timezone.now() + timezone.timedelta(days=30)
    discount = faker.Faker('random_number', digits=2)
    customer = None
    is_use = False

class CartViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = ProductFactory()
        self.product.save()
        self.client.login(username='testuser', password='testpassword')

    def test_get_cart_view(self):
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')

    def test_post_cart_view(self):
        response = self.client.post(reverse('cart'), {'id': self.product.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'1')

class CartListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = ProductFactory()
        self.product.save()
        self.client.login(username='testuser', password='testpassword')
        self.client.post(reverse('cart'), {'id': self.product.id})

    def test_post_cart_list_view(self):
        response = self.client.post(reverse('cart-list'), {'id': self.product.id})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'total': self.product.price, 'count': 0})

        coupon = CouponFactory(customer=self.user)
        coupon.save()
        self.client.session['coupon_id'] = coupon.id
        response = self.client.post(reverse('cart-list'), {'id': self.product.id})
        self.assertEqual(response.status_code, 200)
        total = self.product.price - (self.product.price * coupon.discount / 100)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'total': total, 'count': 0})

class CartCalculatorTestCase(TestCase):
    def setUp(self):
        self.product = ProductFactory()
        self.product.save()
        self.user = UserFactory()
        self.user.save()
        self.client.force_login(self.user)

    def test_post_cart_calculator(self):
        response = self.client.post(reverse('cart-calculator'), {'id': self.product.id, 'btn': 'fa-plus'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(response.content), int(self.product.price))
        
        response = self.client.post(reverse('cart-calculator'), {'id': self.product.id, 'btn': 'fa-minus'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(response.content), 0)

from django.test import RequestFactory, TestCase
from factory.django import DjangoModelFactory
from faker import Faker

from store.models import Product
from store.views import CategorySortView, CategoryView

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = Faker("name")
    category = Faker("word")

class CategoryViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view = CategoryView.as_view()
        self.products = ProductFactory.create_batch(10)
        self.category = self.products[0].category

    def test_get(self):
        request = self.factory.get("/category/{}/".format(self.category))
        response = self.view(request, pk=self.category)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data["count"], 10)
        self.assertEqual(len(response.context_data["products"]), 4)

class CategorySortViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view = CategorySortView.as_view()
        self.products = ProductFactory.create_batch(10)
        self.category = self.products[0].category

    def test_get_sort_asc(self):
        request = self.factory.get("/category/{}/sort/asc/name/".format(self.category))
        response = self.view(request, pk=self.category, sort='asc', attr='name')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context_data["products"]), 10)
        self.assertEqual(response.context_data["products"][0].name, self.products[0].name)

    def test_get_sort_desc(self):
        category = CategoryFactory()
        product1 = ProductFactory(category=category, price=10)
        product2 = ProductFactory(category=category, price=20)
        product3 = ProductFactory(category=category, price=30)
        request = self.factory.get(f'/category/{category.id}/sort/desc/price/')
        view = CategorySortView.as_view()
        response = view(request, pk=category.id, sort='desc', attr='price')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['products'][0], product3)
        self.assertEqual(response.context_data['products'][1], product2)
        self.assertEqual(response.context_data['products'][2], product1)

    def test_get_sort_asc(self):
        category = CategoryFactory()
        product1 = ProductFactory(category=category, price=10)
        product2 = ProductFactory(category=category, price=20)
        product3 = ProductFactory(category=category, price=30)
        request = self.factory.get(f'/category/{category.id}/sort/asc/price/')
        view = CategorySortView.as_view()
        response = view(request, pk=category.id, sort='asc', attr='price')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['products'][0], product1)
        self.assertEqual(response.context_data['products'][1], product2)
        self.assertEqual(response.context_data['products'][2], product3)

    def test_get_sort_asc_invalid_attr(self):
        category = CategoryFactory()
        ProductFactory(category=category, price=10)
        ProductFactory(category=category, price=20)
        ProductFactory(category=category, price=30)
        request = self.factory.get(f'/category/{category.id}/sort/asc/not_exist_attr/')
        view = CategorySortView.as_view()
        response = view(request, pk=category.id, sort='asc', attr='not_exist_attr')
        self.assertEqual(response.status_code, 404)


# ////////////////

from django.test import RequestFactory, TestCase
from faker import Faker
from factory.django import DjangoModelFactory
from store.models import Coupon

class CouponFactory(DjangoModelFactory):
    class Meta:
        model = Coupon

    code = Faker('pystr')
    discount = Faker('random_int', min=10, max=50)
    valid_from = Faker('date_time_this_decade')
    valid_to = Faker('date_time_this_decade', end_datetime='+30d')
    active = True

class CheckoutViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.coupon = CouponFactory()

    def test_apply_coupon(self):
        request = self.factory.get('/')
        request.session = {}

        response = apply_coupon(request, self.coupon.pk)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(request.session['coupon_id'], self.coupon.pk)

    def test_remove_coupon(self):
        request = self.factory.get('/')
        request.session = {'coupon_id': self.coupon.pk}

        response = remove_coupon(request)

        self.assertEqual(response.status_code, 302)
        self.assertIsNone(request.session.get('coupon_id'))
    
    def test_apply_coupon(self):
        coupon = CouponFactory()
        request = self.factory.get('/apply_coupon/')
        request.session = {}
        apply_coupon(request, coupon.id)
        self.assertEqual(request.session.get('coupon_id'), coupon.id)   
    
    def test_apply_coupon_does_not_exist(self):
        request = self.factory.get('/apply_coupon/')
        request.session = {}
        response = apply_coupon(request, 999)
        self.assertEqual(response.status_code, 404)
        
    def test_remove_coupon(self):
        coupon = CouponFactory()
        request = self.factory.get('/remove_coupon/')
        request.session = {'coupon_id': coupon.id}
        remove_coupon(request)
        self.assertIsNone(request.session.get('coupon_id'))
        
    def test_remove_coupon_does_not_exist(self):
        request = self.factory.get('/remove_coupon/')
        request.session = {}
        response = remove_coupon(request)
        self.assertEqual(response.status_code, 404)
        
            
