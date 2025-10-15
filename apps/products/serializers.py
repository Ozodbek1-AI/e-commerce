from rest_framework import serializers

from apps.products.models import Product, Category, Brand, ProductImage
from django.utils.text import slugify

from apps.reviews.models import ProductReview


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


class ProductListSerializer(serializers.ModelSerializer):
    min_price = serializers.SerializerMethodField()
    max_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_min_price(self,obj):
        return obj.price * 0.9

    def get_max_price(self, obj):
        return obj.price * 1.1

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


# class ReviewsSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = ProductReview
#         fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    # reviews = ReviewsSerializers()

    class Meta:
        model = Product
        fields = '__all__'