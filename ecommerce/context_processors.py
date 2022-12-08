from django.core.cache import cache

def message_processor(request):

    notifications = len(cache.get('notifications')) or 0
    noti = cache.get('notifications') or None
    carts = len(request.session.get('cart-duplicate') or [])
    wishlist = len(request.session.get('wishlist') or [])
    notifications = notifications or 0
    noti = noti or None
    currency = request.session.get('currency') or 1
    currency_name = request.session.get('currency_name') or 'USD'

    return {
            'carts': carts,
            'wishlist': wishlist,
            'notifications': notifications,
            'noti': noti,
            'currency': currency,
            'currency_name': currency_name,
        }
