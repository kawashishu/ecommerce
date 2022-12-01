from django.db import models
from customer.models import Customer
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
# Create your models here.

class BillingAddress(models.Model):
    email = models.ForeignKey(Customer, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    countries = CountryField(multiple=False)
    mobilephone = models.CharField(max_length=20, default=None)

    def __str__(self):
        return self.street_address + " " + self.apartment_address + " " + str(self.countries) + " " + self.mobilephone
    class Meta:
        db_table = 'billing_address'
        verbose_name = _('BillingAddress')
