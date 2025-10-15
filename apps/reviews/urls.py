from django.urls import path

from apps.reviews.views import ProductReviewCreateView

app_name = 'reviews'

urlpatterns = [
    path('',ProductReviewCreateView.as_view(),name='create')
]