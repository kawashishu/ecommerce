from django.contrib import admin

from .models import Order, OrderDetail

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'state']
    search_fields = ['id', 'state']
    list_per_page = 20

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail)