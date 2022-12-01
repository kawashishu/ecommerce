from django.contrib import admin

from .models import Product, Notification, Order, OrderDetail, Category



# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'categoryid','quanlity','discount','status','title','price', 'views', 'avatar']
    search_fields = ['categoryid', 'status', 'title', 'price', 'decripstion']
    list_filter = ['categoryid', 'status', 'title', 'price', 'decripstion']

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['content']
    search_fields = ['content']
    list_filter = ['content']

admin.site.register(Product, ProductAdmin)
admin.site.register(Notification, NotificationAdmin) 

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'state']
    search_fields = ['id', 'state']
    list_per_page = 20

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    search_fields = ['name', 'id']
admin.site.register(Category, CategoryAdmin)

