from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ecommerce.views import Index, message_processor

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func.view_class, Index)
    
    