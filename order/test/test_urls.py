from django.test import SimpleTestCase
from django.urls import reverse, resolve
from order.models import Order, OrderDetail
from order.views import BillingView

class TestUrls(SimpleTestCase):

    def test_billing_url_is_resolved(self):
        url = reverse('billing')
        self.assertEquals(resolve(url).func.view_class, BillingView)
    
    