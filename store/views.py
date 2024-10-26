from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *

class ProductView(APIView):

    def get(self, request):
        """
        list of product
        """
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """
        create product
        """
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class ProductUpdateView(APIView):
    def patch(self, request, id):
        """
        update product
        """
        product = Product.objects.get(pk=id)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.error, status=400)
    
class ProductSupplierView(APIView):
    def get(self, request, id):
        """
        list of suppliers of specific product
        """
        product = Product.objects.get(pk=id)
        serializer = ProductSupplierSerializer(product.suppl, many=True)
        return Response(serializer.data, status=200)
    
class OrderView(APIView):

    def post(self, request):
        """
        create order
        """
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class OrderView(APIView):

    def post(self, request):
        """
        create supplier
        """
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    


