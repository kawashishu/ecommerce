import os, time, config
from celery import Celery

from datetime import datetime
from celery import shared_task
from smtplib import SMTPException
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.http import HttpResponse
from requests.exceptions import HTTPError
from django.shortcuts import redirect, render
from store.models import Product
from django.conf import settings
from django.core.cache import cache
from customer.models import Customer
from store.models import Notification
import requests

from django.core.cache.backends.base import DEFAULT_TIMEOUT
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

app = Celery('tasks')
app.config_from_object(config)    #this configures your celery app. Take a look at the config.py file

@shared_task
def get_notification():
    notifications = Notification.objects.all()[:10]
    cache.set('notifications', notifications, timeout=CACHE_TTL)
    
    return HttpResponse(status=200)

@shared_task
def get_api_currency():
    try:
        USD_EUR = requests.get(
            f'https://api.frankfurter.app/latest?amount=1&from=USD&to=EUR').json()['rates']['EUR']
        USD_JPY = requests.get(
            f'https://api.frankfurter.app/latest?amount=1&from=USD&to=JPY').json()['rates']['JPY']
        USD_GBP = requests.get(
            f'https://api.frankfurter.app/latest?amount=1&from=USD&to=GBP').json()['rates']['GBP']
        cache.set('EUR', USD_EUR)
        cache.set('JPY', USD_JPY)
        cache.set('GBP', USD_GBP)
        cache.set('USD', 1)
    except HTTPError as e:
        return HttpResponse(
            {"api": "Cannot load API response"}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    return HttpResponse(status=200)