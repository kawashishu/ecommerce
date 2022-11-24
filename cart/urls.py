from django.urls import include, path
from .views import views


urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('list/', views.CartListView.as_view(), name='cart-list'),
]
