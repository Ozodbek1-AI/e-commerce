from rest_framework import serializers

from apps.products.models import Product
from django.utils.text import slugify

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'slug': {'read_only': True},
            'is_active': {'read_only': True},
        }

    def create(self, validated_data):
        slug = slugify(validated_data.get('name'))
        product = Product.objects.filter(slug=slug)
        while product.exists():
            slug = f"{slug}-{Product.generate_id}"
            product = Product.objects.filter(slug=slug)
        validated_data['slug'] = slug
        return Product.objects.create(**validated_data)
