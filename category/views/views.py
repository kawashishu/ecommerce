from django.shortcuts import render
from django.core.paginator import Paginator
from ..models import Category
from django.views import View
from django.views.generic import ListView


class CategoryView(View):
    
    def get(self, request):
        pass

    def post(self, request):
        pass

    