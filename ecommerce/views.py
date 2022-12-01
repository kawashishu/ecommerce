from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.views.generic import ListView
from requests import session
from store.models import Product
from store.models import Category
from django.core.cache import cache


# Remember: You must convert this shit to CBV ( Class Based View ) to make it good better

PAGINATOR_NUMBER = 8

class Index(ListView):
    model = Category
    template_name = 'index.html'
    paginate_by = PAGINATOR_NUMBER
    context_object_name  = 'categorys'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(status=False)
        context['products'] = products
        return context

def message_processor(request):
    try:
        return len(request.session['cart-duplicate'])
    except:
        return 0