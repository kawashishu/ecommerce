from django.urls import include, path
from .views import views

urlpatterns = [
   path('', views.CheckoutView.as_view() ,name='checkout'),
   
]
