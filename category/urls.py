from django.urls import path
from .views.views import CategoryView


urlspatterns = [
    path('', CategoryView.paginator.as_view(), name='category_paginator'),
]