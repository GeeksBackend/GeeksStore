from rest_framework.routers import DefaultRouter

from apps.carts.views import CartAPI, CartItemAPI


router = DefaultRouter()
router.register('carts', CartAPI, "api_carts")
router.register('carts_items', CartItemAPI, "api_carts_items")

urlpatterns = router.urls