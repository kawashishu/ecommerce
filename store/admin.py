from django.contrib import admin

from .models import Product, Notification


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