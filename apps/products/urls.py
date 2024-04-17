from django.urls import path 

from apps.products.views import ProductAPI, ProductRetrive

urlpatterns = [
    path('', ProductAPI.as_view(), name="api_products"),
    path('<int:pk>/', ProductRetrive.as_view(), name="api_products_detail")
]