from rest_framework import serializers

from apps.products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'user',
                  'image', 'price', 'created', 'category')

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description',
                  'image', 'price', 'created', 'category')