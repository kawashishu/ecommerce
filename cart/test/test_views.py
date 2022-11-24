from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve

from cart.views.views import (
    CartView,
    CartListView,
    remove,
    getTotal,
    getQuanlity,
    getCart,
)

class TestViews(SimpleTestCase):
    
    pass
