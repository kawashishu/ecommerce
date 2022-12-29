from django.db import models
from customer.models import Customer
# Create your models here.


class BillingAddress(models.Model):
    email = models.ForeignKey(
        Customer, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=50, default=None, null=True, blank=True)
    province = models.CharField(
        max_length=100, default=None, null=True, blank=True)
    district = models.CharField(
        max_length=100, default=None, null=True, blank=True)
    ward = models.CharField(
        max_length=100, default=None, null=True, blank=True)
    street_address = models.CharField(
        max_length=100, default=None, null=True, blank=True)
    mobilephone = models.CharField(
        max_length=20, default=None)
    default = models.BooleanField(
        default=False)
    shipping_fee = models.FloatField(default=0)

    def __str__(self):
        return self.province + " " + self.district + " " \
            + str(self.ward) + " " + self.street_address + " " \
            + self.mobilephone

    class Meta:
        db_table = 'billing_address'
