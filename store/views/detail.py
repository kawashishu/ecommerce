
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.views.generic.edit import FormMixin
from comment.models import Comment
from comment.forms import CommentForm
from customer.models import Customer
from ..models import Product


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(productid=self.object)
        self.object.views += 1
        return context


class CreateComment(View):
    def post(self, request, pk):
        content = request.POST.get('content')
        product = int(request.POST.get('product_id'))
        userid = int(request.POST.get('user_id'))
        user = get_object_or_404(Customer, id=userid)
        product = get_object_or_404(Product, id=product)
        comment = Comment.objects.create(
            content=content,
            productid=product,
            customerid=user,
            rating=5,
        )
        comment.save()
        comment = Comment.objects.filter(id=comment.id)
        return JsonResponse({'comment': list(comment.values('content', 'customerid', 'productid', 'rating', 'created'))})


class DeleteComment(View):
    def post(self, request, pk):
        id = int(request.POST.get('comment_id'))
        comment = get_object_or_404(Comment, id=id)
        comment.delete()

        comments = Comment.objects.all()

        return HttpResponse('ok')
