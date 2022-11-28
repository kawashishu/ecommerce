from django.urls import path
from .views.category import CategoryView


urlspatterns = [
    path('', CategoryView.paginator.as_view(), name='category_paginator'),
]