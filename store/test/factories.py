import factory
import factory.fuzzy
from faker import Faker

from store.models import Product, Category, Order, OrderDetail

class CategoryFactory(factory.Factory):
    class Meta:
        model = Category

    name = factory.Faker('name')
    image = factory.Faker('image')
    

class ProductFactory(factory.Factory):
    class Meta:
        model = Product
    
    name = factory.LazyAttribute(lambda x: Faker().name())
    category = factory.SubFactory(CategoryFactory)
    decripstion = factory.LazyAttribute(lambda x: Faker().text())
    quanlity = factory.fuzzy.FuzzyInteger(0, 100)
    discount = factory.fuzzy.FuzzyInteger(0, 100)
    status = factory.fuzzy.FuzzyChoice([True, False])
    title = factory.LazyAttribute(lambda x: Faker().name())
    price = factory.fuzzy.FuzzyFloat(0, 100)
    views = factory.fuzzy.FuzzyInteger(0, 100)
    avatar = factory.LazyAttributeSequence(lambda x, n: f'image_{n}')
    
class OrderFactory(factory.Factory):
    class Meta:
        model = Order
    created = factory.LazyAttribute(lambda x: Faker().date())
    status = factory.fuzzy.FuzzyChoice([True, False])
    
class OrderDetailFactory(factory.Factory):
    class Meta:
        model = OrderDetail
    
    quanlity = factory.fuzzy.FuzzyInteger(0, 100)
    price = factory.fuzzy.FuzzyFloat(0, 100)
    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    

    