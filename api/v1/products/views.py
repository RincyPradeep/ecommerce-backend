from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http.response import HttpResponse
from django.shortcuts import reverse
 
from api.v1.products.serializers import ProductSerializer,CategorySerializer,CartSerializer
from web.models import Product,Category,Cart
 
 
@api_view(["GET"])
@permission_classes([AllowAny])
def products(request):
     instances = Product.objects.filter(is_deleted = False)
     context = {"request" : request}
     serializer = ProductSerializer(instances,many =True,context = context)
     response_data = {
          'status_code' : 6000,
          'data' : serializer.data
     }
     return Response(response_data)


@api_view(["GET"])
@permission_classes([AllowAny])
def singleProduct(request,pk):
     if Product.objects.filter(pk=pk).exists():         
          instance = Product.objects.get(pk=pk)
          context = {"request" : request}
          serializer = ProductSerializer(instance,context = context)
          response_data = {
               'status_code' : 6000,
               'data' : serializer.data
          }
          return Response(response_data)
     else:
          response_data = {
               'status_code' : 6001,
               'message' : 'Product not exist'
          }
          return Response(response_data)


@api_view(["GET"])
def categories(request):
     instances = Category.objects.all()
     serializer = CategorySerializer(instances,many =True)
     return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getcart(request,pk):
     if Cart.objects.filter(user_id=pk).exists():
          instances = Cart.objects.filter(user_id=pk)
          context = {"request" : request}
          serializer = CartSerializer(instances,many =True,context = context)
          response_data = {
               'status_code' : 6000,
               'data' : serializer.data
          }
          return Response(response_data)
     else:
          response_data = {
               'status_code' : 6001,
               'message' : 'Cart not exist'
          }
          return Response(response_data)

     
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def addToCart(request):
     Cart.objects.create(
          user_id = request.data["user_id"],
          product_id = request.data["product_id"],
          quantity = request.data["quantity"]
     )
     response_data = {
          'status_code' : 6000,
          'message' : 'Item added to cart'
     }
     return Response(response_data)