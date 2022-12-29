from .models import BillingAddress
from store.models import OrderItem
from django.contrib import admin


class CheckhoutAdmin(admin.ModelAdmin):
    list_display = ['email', 'province',
                    'district', 'ward', 'street_address', 'mobilephone']
    list_filter = ['email']


# Register your models here.
admin.site.register(BillingAddress, CheckhoutAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'order', 'price',]
    list_filter = ['product', 'order']


admin.site.register(OrderItem, OrderItemAdmin)
