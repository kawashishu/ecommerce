from django.core.cache import cache
from django.shortcuts import redirect


def change_currency(request, pk):
    request.session['currency'] = cache.get(pk)
    request.session['currency_name'] = pk
    request.session.modified = True

    url = request.META.get('HTTP_REFERER')
    return redirect(url)
