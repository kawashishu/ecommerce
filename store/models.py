from django.db import models
from category.models import Category
from customer.models import Customer

# Create your models here.
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
    avatar = models.ImageField(upload_to='images', blank=True, null=True)
    
    class Meta:
        db_table = 'product'
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