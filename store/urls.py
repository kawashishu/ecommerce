
from django.urls import path

from .views import detail, category, cart, currency, search, order, coupon, notification


urlpatterns = [
    path('', search.StoreView.as_view(), name='shop'),
    path('filter/', search.SearchFilterView.as_view(), name='filter'),
    path('search_product/<int:pk>',
         search.SearchCategoryView.as_view(), name='search_by_category'),
     path('search_product/',
         search.SearchAllView.as_view(), name='search_all_product'),
    path('category/productdetail/<int:pk>',
         detail.ProductDetail.as_view(), name='productdetail'),
    path('category/productdetail/<int:pk>/createcomment/',
         detail.CreateComment.as_view(), name='create_comment'),
    path('category/productdetail/<int:pk>/deletecomment/',
         detail.DeleteComment.as_view(), name='delete_comment'),

    path('cart/list/', cart.CartListView.as_view(), name='cart-list'),
    path('cart/', cart.CartView.as_view(), name='cart'),
    # path('wishlist/', cart.WishlistView.as_view(), name='wishlist'),
    path('btn/', cart.CartCalculator.as_view(), name='btn'),

    path('category/<int:pk>', category.CategoryView.as_view(), name='categories'),
    path('category/<int:pk>/<str:attr>/<str:sort>/',
         category.CategorySortView.as_view(), name='sort_categories'),

    path('currency/change/<str:pk>/',
         currency.change_currency, name='change_currency'),

    path('dashboard-order/', order.OrderView.as_view(), name='dash-order'),

    # coupon
    path('apply-coupon/', coupon.ApplyCouponView.as_view(), name='apply_coupon'),
    path('remove-coupon/', coupon.RemoveCouponView.as_view(), name='remove_coupon'),

    # new ui
    path('wish-list/', cart.WishListView.as_view(), name='wish-list'),
    path('remove-wish-list/', cart.RemoveWishListView.as_view(), name='remove-wishlist'),

    # seen notifications
     path('seen-notifications/<int:pk>/', notification.seen_notifications, name='seen-notifications'),
]
