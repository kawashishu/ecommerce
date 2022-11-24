from django.core.cache import cache

def message_processor(request):
    try:
        notifications = len(cache.get('notifications'))
        noti = cache.get('notifications')
    except:
        notifications = 0
        noti = None
        
    try: 
        return {
            'carts': len(request.session['cart-duplicate']),
            'wishlist': len(request.session['wishlist']) or 0,
            'notifications': notifications,
            'noti': noti,
            'currency': request.session['currency'],
            'currency_name': request.session['currency_name'],
        }
    except:
        return {
            'carts': 0,
            'notifications': 0,
            'noti': None,
            'wishlist': 0,
            'currency': 1,
            'currency_name': 'USD',
        }