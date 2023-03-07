# Create your views here.
from django.views.generic import ListView
from store.models import Product
from store.models import Category


PAGINATOR_NUMBER = 8


class Index(ListView):
    model = Category
    template_name = './index.html'
    paginate_by = PAGINATOR_NUMBER
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        products = Product.objects.filter(rating__gte=5).order_by('-views')[:8]
        context = super().get_context_data(**kwargs)
        context['products'] = products
        # get products have discount > 30
        products_sale = Product.objects.filter(discount__gte=30).order_by('-discount')[:4]
        context['products_sale'] = products_sale
        return context


def message_processor(request):
    try:
        return len(request.session.get('cart-duplicate'))
    except KeyError:
        return 0
