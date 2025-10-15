from django.urls import path

from apps.products.views import ProductCreateAPIView, ProductListAPIView, ProductDetailAPIView, ProductUpdateAPIView, \
    ProductPatchUpdateAPIView, ProductDeleteAPIView

app_name = 'products'

urlpatterns = [
    path('',ProductCreateAPIView.as_view(),name='create'),
    path('list/',ProductListAPIView.as_view(),name='list'),
    path('<int:pk>/',ProductDetailAPIView.as_view(),name='detail'),
    path('put/<int:pk>/',ProductUpdateAPIView.as_view(),name='put'),
    path('patch/<int:pk>/',ProductPatchUpdateAPIView.as_view(),name='patch'),
    path('delete/<int:pk>/',ProductDeleteAPIView.as_view(),name='delete'),
]