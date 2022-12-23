from datetime import datetime, timedelta
from django.dispatch import receiver
from django.shortcuts import render
from django.views import View
from store.models import Order, Notification
from django.db.models import signals
from customer.models import Customer
from store.models import Coupon, Notification
from django.contrib.auth.mixins import LoginRequiredMixin


class OrderView(LoginRequiredMixin, View):
    def get(self, request):
        # get 5 last order
        orders = Order.objects.filter(customer=request.user).order_by('-created')[:5]
        orders_count = orders.count()
        context = {
            'orders': orders,
            'orders_count': orders_count,
        }
        return render(request, 'dash-my-order.html', context)


@receiver(signals.post_save, sender=Order)
def create_notifications_order(sender,**kwargs):
    Notification.objects.create(
        customer=kwargs['instance'].customer,
        content=f'Your order is process',
        read=False,
        link='dash-order'
    )


@receiver(signals.post_save, sender=Customer)
def create_notifications_customer(sender,**kwargs):
    Notification.objects.create(
        customer=kwargs['instance'],
        content=f'Welcome to our store {kwargs["instance"]}',
        read=False,
        link='dashboard'
    )
    Coupon.objects.create(
        code='WELCOME',
        discount_amount=10,
        expiration_date=datetime.now() + timedelta(days=30),
        customer=kwargs['instance']
    )

