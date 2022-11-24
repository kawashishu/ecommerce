
from rest_framework import serializers
from ..models import Comment
from customer.serializers import CustomerSerializer


class CommentSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = Comment
        fields = '__all__'
