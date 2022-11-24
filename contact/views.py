from re import template
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from customer.models import Customer

# Create your views here.

class ContactView(View):
    model = Customer
    template_name = 'contact.html'

    def get(self, request):
        return render(request, self.template_name)
        
    def post(self, request):
        pass