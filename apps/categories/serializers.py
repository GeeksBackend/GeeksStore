from rest_framework import serializers

from apps.categories.models import Category
from apps.products.serializers import ProductSerializer

#Serializers - changes one format to another
class CategorySerializer(serializers.ModelSerializer):
    category_products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = "__all__"