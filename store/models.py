from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import models
from customer.models import Customer
from checkout.models import BillingAddress


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images_category', blank=True, null=True)
    class Meta:
        db_table = 'category'
        verbose_name = _('Category')
        
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }
class Product(models.Model):
    name = models.CharField(max_length=200)
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE)
    decripstion = models.TextField()
    quanlity = models.IntegerField()
    discount = models.IntegerField()
    status = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    price = models.FloatField()
    views = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='images_product', blank=True, null=True)
    
    
    class Meta:
        db_table = 'product'
        verbose_name = _('Product')
    def __str__(self):
        return f"{self.name}, {self.categoryid}, {self.decripstion}, {self.quanlity}, {self.discount}, {self.status}, {self.title}, {self.price}, {self.views}, {self.avatar}"
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'decripstion': self.decripstion,
            'price': self.price,
            'quanlity': self.quanlity,
            'discount': self.discount,
            'status': self.status,
            'title': self.title,
            'categoryid': self.categoryid.to_json()
        }

class Notification(models.Model):
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'notification'
        verbose_name = _('Notification')
        

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    billing_address = models.ForeignKey(
        BillingAddress, on_delete=models.CASCADE, null=True)
    state = models.IntegerField(default=1)
    class Meta:
        db_table = 'order'
        verbose_name = _('Order')

    def __str__(self):
        return self.customerid.email
    
class OrderDetail(models.Model):
    quanlity = models.IntegerField()
    price = models.FloatField()
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.quanlity

    class Meta:
        db_table = 'orderdetail'
        verbose_name = _('OrderDetail')

