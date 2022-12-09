
from django import template
from django.core.cache import cache
from django import template


register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
    
@register.filter
def get_session_cart(request, cart):
    return len(request.session[cart])

@register.filter
def get_session_wishlist(request, wishlist):
    return len(request.session[wishlist])

@register.filter
def ranged(min,max):
    return range(min,max)

@register.filter
def price_currency(price, currency):
    if currency is None:
        currency = 1
    return round(price * currency)

@register.filter
def is_active(request, pattern):
    import re
    if re.search(pattern, request.path):
        return 'active'
    return ''

@register.simple_tag
def get_icon_currency(currency):
    if currency == 'USD':
        return '$'
    elif currency == 'EUR':
        return '€'
    elif currency == 'GBP':
        return '£'
    elif currency == 'JPY':
        return '¥'
    return '$'
