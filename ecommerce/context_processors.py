from store.models import Product, Category, Notification, Order, OrderItem
from django.core.paginator import Paginator
from store.views.cart import getTotal


def message_processor(request):

    user = request.user
    if user.is_authenticated:
        notifications = Notification.objects.all().filter(
            customer=user).filter(read=False)
        count_notifications = len(notifications)
        order_items = OrderItem.objects.filter(
            order__in=Order.objects.filter(customer=user).exclude(state='AR'))
        count_order_items = order_items.count()
    else:
        notifications = []
        count_notifications = 0
        count_order_items = 0


    categories = Category.objects.all()
    paginator = Paginator(categories, 5)

    menu_wishlist = request.session.get('wishlist') or []
    wishlist_products = Product.objects.filter(id__in=menu_wishlist)

    shopping_list = request.session.get('cart-duplicate') or []
    carts = len(shopping_list)
    # get product in carts
    shopping_list = Product.objects.filter(id__in=shopping_list)
    # get product in list
    wishlist = len(request.session.get('wishlist') or [])

    currency = request.session.get('currency') or 1
    currency_name = request.session.get('currency_name') or 'USD'
    sub_total = getTotal(request)

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
        'shopping_list': shopping_list,
        'sub_total': sub_total,
        'count_order_items': count_order_items,
    }

def extend_admin_context(request):
    if request.path.startswith('/admin/'):
        # Retrieve the notification data here
        notifications = Notification.objects.all().filter(read=False)
        return {'notifications': notifications}
    return {}