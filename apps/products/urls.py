from django.urls import path

from apps.products.views import ProductCreateAPIView

app_name = 'products'

urlpatterns = [
    path('',ProductCreateAPIView.as_view(),name='create'),
    # path('',ProductCreateAPIView.as_view(),name='create'),
    # path('',ProductCreateAPIView.as_view(),name='create'),
    # path('',ProductCreateAPIView.as_view(),name='create'),
]