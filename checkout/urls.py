from django.urls import include, path
from .views import checkout

urlpatterns = [
   path('', checkout.CheckoutView.as_view() ,name='checkout'),
   
]
