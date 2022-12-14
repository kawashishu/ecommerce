
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

@register.simple_tag
def get_state_number(state):
    if state == 'PR':
        max = 1
    elif state == 'SH':
        max = 2
    elif state == 'EN':
        max = 3
    elif state == 'AR':
        max = 4
    else:
        max = 1
    return max

@register.filter
def ranged(min, max):
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

# template tag multiplication for 1 or more arguments
@register.simple_tag
def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return round(result,2)

@register.simple_tag
def summation(*args):
    result = 0
    for arg in args:
        result += arg
    return round(result,2)

@register.simple_tag
def subtraction(a,b):
    if a <= b:
        return 0
    return round(a-b,2)

@register.simple_tag
def to_int(value):
    return int(value)

