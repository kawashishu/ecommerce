
from django.urls import path
from . import views


urlpatterns = [
    path('', views.getAllProducts,name='getAllProducts'),
    path('cache/customer/', views.view_cached_customer, name='view_cached_customer'),
    path('cache/products/', views.view_cached_products, name='reset_cache_customer'),
]


