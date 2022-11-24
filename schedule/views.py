import datetime
from django.http import HttpResponse
from django.shortcuts import render
from requests import Response
from store.models import Product
from rest_framework import status
from rest_framework.decorators import api_view
from django.conf import settings
from django.core.cache import cache
from customer.models import Customer

# Create your views here.
from django.core.cache.backends.base import DEFAULT_TIMEOUT
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@api_view(['GET'])
def getAllProducts(request):
    products = Product.objects.all()
    results = [ product.to_json() for product in products]
    return HttpResponse(results, status=status.HTTP_200_OK)



@api_view(['GET'])
def view_cached_products(request):
        return HttpResponse(cache.get('products'))

def view_cached_customer(request):
    return HttpResponse(cache.get('customers'))