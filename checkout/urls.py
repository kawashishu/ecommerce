from django.urls import path
from .views import checkout

urlpatterns = [
    path('', checkout.CheckoutView.as_view(), name='checkout'),
    path('set_default_billing_address/', checkout.set_default_billing_address,
         name='set_default_billing_address'),
    path('create_billing_address/',
         checkout.create_billing_address, name='create_billing_address'),
]
