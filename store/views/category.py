from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import DetailView
from store.models import Product


class CategoryView(DetailView):
    model = Product
    template_name = 'shop.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs['pk'])
        products = Product.objects.filter(category=self.kwargs['pk'])
        count = products.count()
        related_search = self.request.session.get('related_search') or []
        paginator = Paginator(products, self.paginate_by)
        page_number = self.request.GET.get("page")
        try:
            contacts = paginator.page(page_number)
            print("try")
        except PageNotAnInteger:
            contacts = paginator.page(1)
            print("PageNotAnInteger")
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
            print("EmptyPage")
        context = {
            'products': contacts,
            'count': count,
            'related_search': related_search,
        }
        print("context")
        return context


class CategorySortView(DetailView):
    model = Product
    template_name = 'shop.html'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sort = self.kwargs['sort']
        attr = self.kwargs['attr']

        if sort == 'asc':
            context['products'] = Product.objects.filter(
                category=self.kwargs['pk']).order_by(attr)
        else:
            context['products'] = Product.objects.filter(
                category=self.kwargs['pk']).order_by(f'-{attr}')

        return context
