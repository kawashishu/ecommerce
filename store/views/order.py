from django.shortcuts import render
from django.views import View
from store.models import Order

class BillingView(View):
    def get(self,*args, **kwargs):
        order = Order.objects.all()
        context = {
            'order': order,
        }
        return render(self.request, "billing.html", context)