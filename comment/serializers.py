from rest_framework.serializers import ModelSerializer

from store.models import Product

from .models import Comment
from customer.models import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "name", "email", "phone", "is_active"]


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'decripstion']


class CommentSerializer(ModelSerializer):
    customer = CustomerSerializer()
    product = ProductSerializer()

    class Meta:
        model = Comment
        fields = ["id", "content", "customer", "product", "rating", "created"]
