from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, UserViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
