from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from store.models import Category, Product


class CategoryView(DetailView):
    model = Product
    template_name = 'shop.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(categoryid=self.kwargs['pk'])
        paginator = Paginator(products, self.paginate_by)
        page_number = self.request.GET.get("page")
        print(page_number)
        try:
            contacts = paginator.page(page_number)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        print(contacts)
        context['products'] = contacts
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
                categoryid=self.kwargs['pk']).order_by(attr)
        else:
            context['products'] = Product.objects.filter(
                categoryid=self.kwargs['pk']).order_by(f'-{attr}')

        return context
