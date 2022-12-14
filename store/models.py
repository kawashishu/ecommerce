from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import models
from customer.models import Customer
from checkout.models import BillingAddress


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images_category', blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    class Meta:
        db_table = 'category'
        
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    decripstion = models.TextField()
    quantity = models.IntegerField()
    discount = models.IntegerField()
    status = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    price = models.FloatField()
    views = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='images_product', blank=True, null=True)
    
    class Meta:
        db_table = 'product'
    def __str__(self):
        return f"{self.name}, {self.category}, {self.decripstion}, {self.quanlity}, {self.discount}, {self.status}, {self.title}, {self.price}, {self.views}, {self.avatar}"
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
            'category': self.category.to_json()
        }

class ProductImage(models.Model):
    image = models.ImageField(upload_to='images_product', blank=True, null=True)
    product = models.ForeignKey(Product, related_name='images' , on_delete=models.CASCADE)
    class Meta:
        db_table = 'productimage'
    def __str__(self):
        return self.image
    

class Notification(models.Model):
    content = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    read = models.BooleanField(default=False)
    def __str__(self):
        return self.content

    class Meta:
        db_table = 'notification'
        


class Order(models.Model):
    PROCESS = 'PR'
    SHIPPED = 'SH'
    ENROUTE = 'EN'
    ARRIVE = 'AR'

    ORDER_STATUS_CHOICES = [
        (PROCESS, 'Processing'),
        (SHIPPED, 'Shipped'),
        (ENROUTE, 'Enroute'),
        (ARRIVE, 'Arrived'),
    ]

    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    billing_address = models.ForeignKey(
        BillingAddress, on_delete=models.CASCADE, null=True)
    # field state with 4 choice ( New, Processing, Shipping, Completed)
    state = models.CharField(
        max_length=2,
        choices=ORDER_STATUS_CHOICES,
        default=PROCESS,
    )



    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.customer.email
    
class OrderDetail(models.Model):
    quanlity = models.IntegerField()
    price = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.quanlity

    class Meta:
        db_table = 'orderdetail'

class Coupon(models.Model):
    code = models.CharField(max_length=50)
    expiration_date = models.DateField()
    discount_amount = models.DecimalField(max_digits=5, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='coupons', default=None, blank=True, null=True)

    class Meta:
        db_table = 'coupon'
    
    def __str__(self):
        return self.code