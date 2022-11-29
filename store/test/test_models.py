from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from category.models import Category
from store.models import Product


class TestModel(TestCase):
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
