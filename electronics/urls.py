from electronics.apps import ElectronicsConfig
from rest_framework.routers import DefaultRouter

from electronics.views import SellerViewSet, ProductViewSet, ContactViewSet

app_name = ElectronicsConfig.name

router = DefaultRouter()
router.register(r'seller', SellerViewSet, basename='seller')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'contact', ContactViewSet, basename='contact')


urlpatterns = [] + router.urls
