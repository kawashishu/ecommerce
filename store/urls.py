
from django.urls import path
from .views import detail, category, cart, currency, search, order, coupon


urlpatterns = [
    path('', search.StoreView.as_view() ,name='shop'),
    path ('filter/<int:pk>', search.SearchFilterView.as_view(), name='filter'),
    path('search_product/<int:pk>', search.SearchFormView.as_view(), name='search_product'),
     
    path('category/productdetail/<int:pk>', detail.ProductDetail.as_view(), name = 'productdetail'),
    path('category/productdetail/<int:pk>/createcomment/', detail.CreateComment.as_view(), name = 'create_comment'),
    path('category/productdetail/<int:pk>/deletecomment/', detail.DeleteComment.as_view(), name = 'delete_comment'),
    
    path('cart/list/', cart.CartListView.as_view(), name='cart-list'),
    path('cart/', cart.CartView.as_view(), name='cart'),
    path('wishlist/', cart.WishlistView.as_view(), name='wishlist'),
    path('btn/', cart.CartCalculator.as_view(), name='btn'),
    
    path('category/<int:pk>', category.CategoryView.as_view(), name='categories'),
    path('category/<int:pk>/<str:attr>/<str:sort>/', category.CategorySortView.as_view(), name='sort_categories'),

    path('currency/change/<str:pk>/', currency.change_currency, name='change_currency'),
    
    path('billing/', order.BillingView.as_view() ,name='billing'),

    # coupon
    path('coupon/', coupon.ApplyCouponView.as_view(), name='apply_coupon'),

]