from django.db import models

from customer.models import Customer
from store.models import Product

# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content


    class Meta:
        db_table = 'comment'