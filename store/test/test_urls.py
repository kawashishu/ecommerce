from django.test import SimpleTestCase
from django.urls import reverse, resolve

from store.views import detail, category, cart, currency, search, order

class TestUrls(SimpleTestCase):
    def test_search_url_is_resolved(self):
        url = reverse('shop')
        self.assertEquals(resolve(url).func.view_class, search.StoreView)
        
    def test_search_filter_url_is_resolved(self):
        url = reverse('filter')
        self.assertEquals(resolve(url).func.view_class, search.SearchFilterView)
    
    def test_productdetail_url_is_resolved(self):
        url = reverse('productdetail', args=[1])
        self.assertEquals(resolve(url).func.view_class, detail.ProductDetail)
        
    def test_search_product_url_is_resolved(self):
        url = reverse('search_product')
        self.assertEquals(resolve(url).func.view_class, search.SearchFormView)
        
    def test_create_comment_url_is_resolved(self):
        url = reverse('create_comment', args=[1])
        self.assertEquals(resolve(url).func.view_class, detail.CreateComment)
        
    def test_delete_comment_url_is_resolved(self):
        url = reverse('delete_comment', args=[1])
        self.assertEquals(resolve(url).func.view_class, detail.DeleteComment)
    
    def test_wishlist_url_is_resolved(self):
        url = reverse('wishlist')
        self.assertEquals(resolve(url).func.view_class, cart.WishlistView)
    
    def test_btn_url_is_resolved(self):
        url = reverse('btn')
        self.assertEquals(resolve(url).func.view_class, cart.CartCalculator)
        
    def test_change_currency_url_is_resolved(self):
        url = reverse('change_currency', args=['USD'])
        self.assertEquals(resolve(url).func, currency.change_currency)
    
    def test_categories_url_is_resolved(self):
        url = reverse('categories', args=[1])
        self.assertEquals(resolve(url).func.view_class, category.CategoryView)
        
    def test_sort_categories_url_is_resolved(self):
        url = reverse('sort_categories', args=[1, 'name', 'asc'])
        self.assertEquals(resolve(url).func.view_class, category.CategorySortView)

    def test_cart_url_is_resolved(self):
        url = reverse('cart')
        self.assertEquals(resolve(url).func.view_class, cart.CartView)

    def test_cart_list_url_is_resolved(self):
        url = reverse('cart-list')
        self.assertEquals(resolve(url).func.view_class, cart.CartListView)

    def test_billing_url_is_resolved(self):
        url = reverse('billing')
        self.assertEquals(resolve(url).func.view_class, order.BillingView)