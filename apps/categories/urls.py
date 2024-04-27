from rest_framework.routers import DefaultRouter

from apps.categories.views import CategoryAPI

router = DefaultRouter()
router.register('categories', CategoryAPI, "api_categories")

urlpatterns = router.urls