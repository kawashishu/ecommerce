
from django.urls import reverse_lazy
from ..models import Comment
from django.views.generic import CreateView, DeleteView, UpdateView


# Create your views here.


class AddComment(CreateView):
    model = Comment
    template_name = 'product_detail.html'

    def form_valid(self, form):
        form.instance.product = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('product_detail')


class UpdateComment(UpdateView):
    model = Comment
    template_name = 'product_detail.html'
    success_url = reverse_lazy('product_detail')


class DeleteComment(DeleteView):
    model = Comment
    template_name = 'product_detail.html'
    success_url = reverse_lazy('product_detail')
