from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework import status
from .forms import TestForm
from rest_framework import viewsets
# Create your views here.

def home(request):
    form = TestForm()
    return render(request, 'test_app/index.html', {'form' : form})

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

# @api_view(['GET',"POST"])
# def product_collection(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         print(request.POST)
#         serializer = ProductSerializer(data = request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             print("success")
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','DELETE', 'PUT'])
# def product_element(request, pk):

#     try:
#         product = Product.objects.get(pk=pk)
#     except:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         product = Product.objects.get(pk=pk)
#         product.delete()
#         print("delete successful")
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product, data = request.POST)
#         if serializer.is_valid():
#             print("Update is valid")
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
