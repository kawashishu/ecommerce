
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from comment.models import Comment
from customer.models import Customer
from ..models import Product


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(product=self.object)
        context['products'] = Product.objects.filter(
            category=self.object.category).exclude(id=self.object.id)
        self.object.views += 1
        return context


class CreateComment(View):
    def post(self, request, pk):
        content = request.POST.get('content')
        product = int(request.POST.get('product'))
        userid = int(request.POST.get('user'))
        user = get_object_or_404(Customer, id=userid)
        product = get_object_or_404(Product, id=product)
        comment = Comment.objects.create(
            content=content,
            product=product,
            customer=user,
            rating=5,
        )
        comment.save()
        comment = Comment.objects.filter(id=comment.id)
        return JsonResponse({'comment': list(comment.values('id', 'content', 'customer', 'product', 'rating', 'created')), 'user': user.name})


class DeleteComment(View):
    def post(self, request, pk):
        id = int(request.POST.get('comment_id'))
        comment = get_object_or_404(Comment, id=id)
        comment.delete()

        return HttpResponse(HttpResponse.status_code)
