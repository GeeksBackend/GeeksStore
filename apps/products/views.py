from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.products.models import Product
from apps.products.serializers import ProductSerializer, ProductCreateSerializer
from apps.products.permissions import ProductPermission

# Create your views here.
class ProductAPI(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProductCreateSerializer
        return ProductSerializer
    
class ProductRetrive(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

    def get_permissions(self):
        if self.request.method in ('DELETE', 'PUT', 'PATCH'):
            return (ProductPermission(), )
        return (AllowAny(), )