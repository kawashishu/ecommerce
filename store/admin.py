from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Product, Notification, Order, \
    Category, Coupon, ProductImage, DetailProduct


# Register your models here.
class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'quantity', 'discount',
                    'status', 'title', 'price', 'views', 'avatar']
    search_fields = ['category', 'status', 'title', 'price', 'decripstion']
    list_filter = ['category', 'status', 'title', 'price', 'decripstion']
    inlines = [ProductImageInline]


class DetailProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'width', 'height', 'weight', 'length']
    search_fields = ['product', 'width', 'height', 'weight', 'length']
    list_filter = ['product', 'width', 'height', 'weight', 'length']


admin.site.register(DetailProduct, DetailProductAdmin)


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['content', 'customer', 'read']
    search_fields = ['content']
    list_filter = ['content']


admin.site.register(Product, ProductAdmin)
admin.site.register(Notification, NotificationAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description']
    search_fields = ['name', 'id']


admin.site.register(Category, CategoryAdmin)


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'expiration_date', 'discount_amount']


admin.site.register(Coupon, CouponAdmin)

def calculate_revenue_stats(orders):
    
    return "revenue_stats"

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id',  'customer', 'billing_address']
    search_fields = ['id','customer', 'billing_address']
    list_per_page = 20

    actions = ['calculate_revenue_stats']

    def calculate_revenue_stats(self, request, queryset):
        # Retrieve the selected orders
        orders = queryset.all()
        # Calculate the revenue statistics
        stats = calculate_revenue_stats(orders)
        # Display the revenue statistics in the Django admin interface
        self.message_user(request, _('Revenue statistics: %(stats)s') % {'stats': stats})
 
admin.site.register(Order, OrderAdmin)




