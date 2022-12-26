# Create your views here.
from django.views.generic import ListView
from store.models import Product
from store.models import Category


PAGINATOR_NUMBER = 8


class Index(ListView):
    model = Category
    template_name = 'index.html'
    paginate_by = PAGINATOR_NUMBER
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        products = Product.objects.filter(status=False)
        context = super().get_context_data(**kwargs)
        context['products'] = products
        return context


def message_processor(request):
    try:
        return len(request.session['cart-duplicate'])
    except KeyError:
        return 0
