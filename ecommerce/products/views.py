from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can manage products

    # Implement filtering
    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category')
        price_min = self.request.query_params.get('price_min')
        price_max = self.request.query_params.get('price_max')
        if category:
            queryset = queryset.filter(category=category)
        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)
        return queryset

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer