from django.urls import include, path
from .views import checkout

urlpatterns = [
   path('', checkout.CheckoutView.as_view() ,name='checkout'),
   path('save_billing_address/', checkout.save_billing_address, name='save_billing_address'),
   path('set_default_billing_address/', checkout.set_default_billing_address, name='set_default_billing_address'),
   path('set_shipping_fee/', checkout.set_shipping_fee, name='set_shipping_fee'),
]
