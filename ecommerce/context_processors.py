from store.models import Product, Category, Notification
from django.core.paginator import Paginator

def message_processor(request):

    user = request.user
    if user.is_authenticated:
        notifications = Notification.objects.all().filter(customer=user).filter(read=False)
        count_notifications = len(notifications)
    else:
        notifications = []
        count_notifications = 0

    categories = Category.objects.all()
    paginator = Paginator(categories, 5)
    
    menu_wishlist = request.session.get('wishlist') or []
    wishlist_products = Product.objects.filter(id__in=menu_wishlist)

    carts = len(request.session.get('cart-duplicate') or [])
    wishlist = len(request.session.get('wishlist') or [])

    currency = request.session.get('currency') or 1
    currency_name = request.session.get('currency_name') or 'USD'
    
    return {
            'carts': carts,
            'wishlist': wishlist,
            'count_notifications': count_notifications,
            'notifications': notifications,
            'currency': currency,
            'currency_name': currency_name,
            'wishlist_products': wishlist_products,
            'categories': categories,
            'paginator': paginator,
        }
