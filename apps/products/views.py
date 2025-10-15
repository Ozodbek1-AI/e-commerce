from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.products.serializers import ProductModelSerializer


class ProductCreateAPIView(APIView):
    serializer_class = ProductModelSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def get(self):
        pass