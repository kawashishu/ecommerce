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
        price_pre = int(request.GET.get('price_min'))
        price_next = int(request.GET.get('price_max'))
        pk = int(request.GET.get('pk'))
        products = Product.objects.filter(price__range=(
            price_pre, price_next)).filter(
            category=pk)
        return JsonResponse({'products': list(products.values('title', 'price', 'id', 'avatar','decripstion'))})


class SearchCategoryView(View):
    def get(self, request, pk):
        query = request.GET.get('query')
        products = cache.get('products')
        products = Product.objects.filter(title__icontains=query).filter(
            category=pk)

        return JsonResponse({'products': list(products.values('title', 'price', 'id', 'avatar','decripstion'))})

class SearchAllView(View):
    def get(self, request):
        query = request.GET.get('query')   
        if 'related_search' in request.session:
            request.session['related_search'].insert(0, query)
            if len(request.session['related_search']) > 5:
                request.session['related_search'].pop(len(request.session['related_search']) - 1)
        else:
            request.session['related_search'] = [query]

        request.session.modified = True
        related_search = request.session.get('related_search') or []
        products = Product.objects.filter(decripstion__icontains=query)

        context = {
            'products': products,
            'related_search': related_search,
        }
        return render(request, 'shop.html', context=context)
