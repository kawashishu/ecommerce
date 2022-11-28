import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from requests import Response
from order.models import Order
from store.models import Product
from rest_framework import status
from rest_framework.decorators import api_view
from django.conf import settings
from django.core.cache import cache
from customer.models import Customer


class BillingView(View):
    def get(self,*args, **kwargs):
        order = Order.objects.all()
        context = {
            'order': order,
        }
        return render(self.request, "billing.html", context)
