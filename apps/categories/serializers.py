from rest_framework import serializers

from apps.categories.models import Category

#Serializers - changes one format to another
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"