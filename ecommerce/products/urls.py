from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDeleteView, ProductSearchView, CategoryListCreateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDeleteView.as_view(), name='product-detail'),
    path('search/', ProductSearchView.as_view(), name='product-search'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
]



urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
