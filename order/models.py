from django.db import models
from customer.models import Customer
from store.models import Product
from checkout.models import BillingAddress
# Create your models here.
class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    billing_address = models.ForeignKey(
        BillingAddress, on_delete=models.CASCADE, null=True)
    state = models.IntegerField(default=1)
    email = models.CharField(max_length=200)
    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.email

class OrderDetail(models.Model):
    quanlity = models.IntegerField()
    price = models.FloatField()
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.quanlity

    class Meta:
        db_table = 'orderdetail'

