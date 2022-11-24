from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from customer.models import Customer

class ModelTest(TestCase):
        
    def setUp(self):
        self.Customer = Customer.objects.create_user(
            name = 'test',
            email = 'test@gmail.com',
            phone = '132123',
            password = '123456',
        )        
    def test_customer_model(self):
        print(self.Customer)
        self.assertEqual(self.Customer.name, 'test')
        self.assertEqual(self.Customer.email, 'test@gmail.com')
        
        