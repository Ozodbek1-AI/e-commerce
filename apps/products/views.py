from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.products.models import Product
from apps.products.serializers import ProductModelSerializer, ProductDetailSerializer, ProductUpdateSerializer


#Product create
class ProductCreateAPIView(APIView):
    serializer_class = ProductModelSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

#Product list
class ProductListAPIView(APIView):
    def get(self,request):
        products = Product.objects.filter(is_active=True)

        category = request.query_params.get('category')
        brand = request.query_params.get('brand')
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        is_featured = request.query_params.get('is_featured')
        search = request.query_params.get('search')

        if category:
            products = products.filter(category_id=category)

        if brand:
            products = products.filter(brand_id=brand)

        if min_price:
            products = products.filter(min_price_id=min_price)

        if max_price:
            products = products.filter(max_price_id=max_price)

        if is_featured:
            products = products.filter(is_featured=is_featured.lower() == 'true')

        if search:
            products = products.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
            )

        serializer = ProductModelSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Product detail
class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)

#Product Update
class ProductUpdateAPIView(APIView):
    def put(self,request,pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error':'Product not found'},status=404)

        serializer = ProductUpdateSerializer(instance=product,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Product updated", "data": serializer.data},
                status=status.HTTP_200_OK
            )

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
