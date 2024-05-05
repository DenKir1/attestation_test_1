from electronics.apps import ElectronicsConfig
from rest_framework.routers import DefaultRouter

from electronics.views import SellerViewSet

app_name = ElectronicsConfig.name

router = DefaultRouter()
router.register(r'seller', SellerViewSet, basename='seller')


urlpatterns = [] + router.urls
