
from celery import shared_task
from smtplib import SMTPException
from django.core.mail import EmailMessage
from django.http import HttpResponse
from requests.exceptions import HTTPError
from store.models import Product
from django.conf import settings
from django.core.cache import cache
from customer.models import Customer
from store.models import Notification
import requests

from django.core.cache.backends.base import DEFAULT_TIMEOUT
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@shared_task
def send_email():
    users = Customer.objects.all()
    for user in users:
        email = user.email
        mail_subject = 'Dear Customer'
        message = "We have a new product so hot, \
        come and buy it. Give me your money, please.......!"
        send_email = EmailMessage(mail_subject, message, to=[email])
        try:
            send_email.send()
            return HttpResponse(status=200)
        except SMTPException:
            return HttpResponse(status=400)


@shared_task
def super_sales():
    products = Product.objects.all()
    for product in products:
        product.price *= 0.5
        product.save()

    return HttpResponse(status=200)


@shared_task
def reset_product():
    products = Product.objects.all()
    for product in products:
        product.price *= 2
        product.save()


@shared_task
def get_notification():
    notifications = Notification.objects.all()[:10]
    cache.set('notifications', notifications, timeout=CACHE_TTL)


@shared_task
def get_api_currency():
    try:
        USD_EUR = requests.get(
            'https://api.frankfurter.app/latest?amount=1&from=USD&to=EUR').\
            json()['rates']['EUR']
        USD_JPY = requests.get(
            'https://api.frankfurter.app/latest?amount=1&from=USD&to=JPY').\
            json()['rates']['JPY']
        USD_GBP = requests.get(
            'https://api.frankfurter.app/latest?amount=1&from=USD&to=GBP').\
            json()['rates']['GBP']

        cache.set('EUR', USD_EUR)
        cache.set('JPY', USD_JPY)
        cache.set('GBP', USD_GBP)
        cache.set('USD', 1)
    except HTTPError:
        return HttpResponse(status=400)
