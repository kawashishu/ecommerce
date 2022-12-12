from django.shortcuts import render
from django.views import View
from store.models import Order

class BillingView(View):
    def get(self,*args, **kwargs):
        user = self.request.user
        order = Order.objects.filter(customer=user)
        context = {
            'order': order,
        }
        return render(self.request, "billing.html", context)