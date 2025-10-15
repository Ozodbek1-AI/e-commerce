from django.urls import path

from apps.products.views import ProductCreateAPIView, ProductListAPIView

app_name = 'products'

urlpatterns = [
    path('',ProductCreateAPIView.as_view(),name='create'),
    path('list/',ProductListAPIView.as_view(),name='list'),
    # path('',ProductCreateAPIView.as_view(),name='create'),
    # path('',ProductCreateAPIView.as_view(),name='create'),
]