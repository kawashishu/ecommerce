from django.contrib import admin

from .models import Product, Notification, Order, OrderDetail, Category, Coupon, ProductImage
from customer.models import Customer



# Register your models here.
class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category','quanlity','discount','status','title','price', 'views', 'avatar']
    search_fields = ['category', 'status', 'title', 'price', 'decripstion']
    list_filter = ['category', 'status', 'title', 'price', 'decripstion']
    inlines = [ProductImageInline]


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['content', 'customer', 'read']
    search_fields = ['content']
    list_filter = ['content']

admin.site.register(Product, ProductAdmin)
admin.site.register(Notification, NotificationAdmin) 

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'state','customer', 'billing_address']
    search_fields = ['id', 'state']
    list_per_page = 20

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    search_fields = ['name', 'id']
admin.site.register(Category, CategoryAdmin)

class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'expiration_date', 'discount_amount']
    
admin.site.register(Coupon, CouponAdmin)



