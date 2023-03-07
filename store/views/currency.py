from django.core.cache import cache
from django.shortcuts import redirect


# create hash table for currency
def create_currency(request):
    currency = {
        'USD': 1,
        'EUR': 0.85,
        'GBP': 0.75,
        'JPY': 7.5,
    }

    for key, value in currency.items():
        cache.set(key, value)
    return 0


def change_currency(request, pk):
    create_currency(request)
    request.session['currency'] = cache.get(pk)
    request.session['currency_name'] = pk
    request.session.modified = True

    url = request.META.get('HTTP_REFERER')
    return redirect(url)
