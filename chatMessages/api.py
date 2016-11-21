from .views import ChatMessageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
orders_router = router.register(r'messages', ChatMessageViewSet, base_name='couriers')

urlpatterns = router.urls
