from .models import BillingAddress
from django.contrib import admin

class CheckhoutAdmin(admin.ModelAdmin):
    list_display = ['email', 'street_address', 'apartment_address', 'countries']
    list_filter = ['email']

# Register your models here.
admin.site.register(BillingAddress, CheckhoutAdmin)