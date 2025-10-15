from django.urls import path

from apps.products.views import ProductCreateAPIView, ProductListAPIView, ProductDetailAPIView

app_name = 'products'

urlpatterns = [
    path('',ProductCreateAPIView.as_view(),name='create'),
    path('list/',ProductListAPIView.as_view(),name='list'),
    path('<int:pk>/',ProductDetailAPIView.as_view(),name='detail'),
    # path('',ProductCreateAPIView.as_view(),name='create'),
]