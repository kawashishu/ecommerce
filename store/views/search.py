import requests
from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from ..models import Product

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


STEP_FILTER_PRICE = 20


class StoreView(ListView):
    model = Product
    template_name = 'shop.html'
    paginate_by = 9
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SearchFilterView(View):
    def get(self, request):
        price = int(request.GET.get('price'))
        products = Product.objects.filter(price__range=(
            price * STEP_FILTER_PRICE, price * STEP_FILTER_PRICE + STEP_FILTER_PRICE))
        return JsonResponse({'products': list(products.values('title', 'price', 'id', 'avatar',))})


class SearchFormView(View):
    def get(self, request):
        query = request.GET.get('query')
        products = cache.get('products')
        products = Product.objects.filter(title__icontains=query)

        return JsonResponse({'products': list(products.values('title', 'price', 'id', 'avatar',))})
