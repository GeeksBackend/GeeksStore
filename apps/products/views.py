from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.products.models import Product
from apps.products.serializers import ProductSerializer, ProductCreateSerializer
from apps.products.permissions import ProductPermission

# Create your views here.
class ProductAPI(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProductCreateSerializer
        return ProductSerializer
    
    def get_permissions(self):
        if self.request.method in ('DELETE', 'PUT', 'PATCH'):
            return (ProductPermission(), )
        return (AllowAny(), )