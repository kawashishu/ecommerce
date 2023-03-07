from datetime import datetime, timedelta
from django.dispatch import receiver
from django.shortcuts import render
from django.views import View
from store.models import Order, Notification, Coupon, OrderItem
from django.db.models import signals
from customer.models import Customer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
import random


class OrderView(LoginRequiredMixin, View):
    def get(self, request):
        # get 5 last order
        orders = Order.objects.filter(customer=request.user).\
            order_by('-created')[:5]
        order_items = OrderItem.objects.filter(order__in=orders)
        orders_items_count = order_items.count()
        context = {
            'orders': orders,
            'order_items': order_items,
            'orders_items_count': orders_items_count,
            'shipping-fee': 0,
        }
        return render(request, 'dash-my-order.html', context)


@receiver(signals.post_save, sender=Order)
def create_notifications_order(sender, **kwargs):
    Notification.objects.create(
        customer=kwargs['instance'].customer,
        content='Your order is processing',
        read=False,
        link='dash-order'
    )


class ManageOrderView(LoginRequiredMixin, DetailView):
    model = OrderItem
    template_name = 'dash-manage-order.html'
    context_object_name = 'order_item'


@receiver(signals.post_save, sender=Customer)
def create_notifications_customer(sender, **kwargs):
    Notification.objects.create(
        customer=kwargs['instance'],
        content=f'Welcome to our store {kwargs["instance"]}',
        read=False,
        link='dashboard'
    )
    Coupon.objects.create(
        code='WELCOME',
        discount_amount=random.randint(10, 50),
        expiration_date=datetime.now() + timedelta(days=30),
        customer=kwargs['instance'],
        image='images_coupon/coupon.png',
    )
