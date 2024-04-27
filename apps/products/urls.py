from rest_framework.routers import DefaultRouter

from apps.products.views import ProductAPI

router = DefaultRouter()
router.register('products', ProductAPI, "api_products")

urlpatterns = router.urls