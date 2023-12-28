from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, ProductItemViewSet, ProductItemTransitionViewSet

router = DefaultRouter()
router.register("product", ProductViewSet, basename="product")
router.register("item", ProductItemViewSet, basename="product_item")
router.register("transition", ProductItemTransitionViewSet, basename="product_transition")
urlpatterns = router.urls
