from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from customer.models import Customer
from customer.test.factories import CustomerFactory
class CustomerModelTest(TestCase):
        
    def setUp(self):
        self.customer = CustomerFactory()
        
    def test_customer_model(self):
        assert self.customer.name == self.customer.name
        assert self.customer.email == self.customer.email  
        assert self.customer.phone == self.customer.phone
        assert self.customer.address == self.customer.address
        assert self.customer.status == self.customer.status
        assert self.customer.avatar == self.customer.avatar
        assert self.customer.age == self.customer.age
        assert self.customer.is_active == self.customer.is_active
        assert self.customer.is_staff == self.customer.is_staff

        
        
        