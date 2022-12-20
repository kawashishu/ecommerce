from datetime import datetime, timedelta
from django.dispatch import receiver
from django.shortcuts import render
from django.views import View
from store.models import Order, Notification
from django.db.models import signals
from customer.models import Customer
from store.models import Coupon, Notification


class BillingView(View):
    def get(self,*args, **kwargs):
        user = self.request.user
        order = Order.objects.filter(customer=user)
        context = {
            'order': order,
        }
        return render(self.request, "billing.html", context)


@receiver(signals.post_save, sender=Order)
def create_notifications_order(sender,**kwargs):
    print(kwargs['instance'])
    Notification.objects.create(
        customer=kwargs['instance'].customer,
        content=f'Your order {kwargs["instance"]} has been placed',
        read=False,
        link='billing'
    )


@receiver(signals.post_save, sender=Customer)
def create_notifications_customer(sender,**kwargs):
    print(kwargs['instance'])
    Notification.objects.create(
        customer=kwargs['instance'],
        content=f'Welcome to our store {kwargs["instance"]}, go to profile to update your information',
        read=False,
        link='dashboard'
    )
    Coupon.objects.create(
        code='WELCOME',
        discount_amount=10,
        expiration_date=datetime.now() + timedelta(days=30),
        customer=kwargs['instance']
    )