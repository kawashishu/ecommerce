from faker import Faker
import factory
import factory.fuzzy

from customer.models import Customer

class CustomerFactory(factory.Factory):
    class Meta:
        model = Customer

    name = factory.LazyAttribute(lambda x: Faker().name())
    email = factory.LazyAttribute(lambda x: Faker().email())
    phone = factory.LazyAttribute(lambda x: Faker().phone_number())
    address = factory.LazyAttribute(lambda x: Faker().address())
    status = factory.fuzzy.FuzzyChoice([True, False])
    status = factory.fuzzy.FuzzyChoice([True, False])
    avatar = factory.LazyAttributeSequence(lambda x, n: f'image_{n}')
    age = factory.fuzzy.FuzzyInteger(0, 100)
    sex = factory.fuzzy.FuzzyChoice([True, False])
    is_active = factory.fuzzy.FuzzyChoice([True, False])
    is_staff = factory.fuzzy.FuzzyChoice([True, False])
    
    