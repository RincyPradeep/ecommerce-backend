from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
 
from api.v1.products.serializers import ProductSerializer,CategorySerializer,CartSerializer,OrderSerializer,BannerSerializer,WishlistSerializer
from products.models import Product,Category,Cart,Order,Banner,Wishlist

from django.contrib.auth.models import User
 
 
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
          
     else:
          response_data = {
               'status_code' : 6001,
               'message' : 'Product not exist'
          }
     return Response(response_data)


@api_view(["GET"])
@permission_classes([AllowAny])
def categories(request):
     instances = Category.objects.all()
     context = {"request" : request}
     serializer = CategorySerializer(instances,many =True,context = context)
     response_data = {
          'status_code' : 6000,
          'data' : serializer.data
     }
     return Response(response_data)


@api_view(["GET"])
@permission_classes([AllowAny])
def category_products(request,pk):
     if Product.objects.filter(category_id=pk).exists():
          instances = Product.objects.filter(category_id=pk)
          context = {"request" : request}
          serializer = ProductSerializer(instances,many =True,context = context)
          response_data = {
               'status_code' : 6000,
               'data' : serializer.data
          }
     else:
          response_data = {
               'status_code' : 6001,
               'message' : 'Category not exist'
          }
     return Response(response_data)


@api_view(["GET"])
@permission_classes([AllowAny])
def search(request):   
     instances = Product.objects.filter(is_deleted = False)
     q = request.GET.get("q")
     if q:
          instances = instances.filter(Q(title__icontains = q) | Q(description__icontains = q) | Q(category__name__icontains = q) )
     context = {"request" : request}
     serializer = ProductSerializer(instances,many =True,context = context)
     response_data = {
          'status_code' : 6000,
          'data' : serializer.data
     }
     return Response(response_data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getcart(request,pk):
     if not(User.objects.filter(id = pk)).exists():
          response_data = {
               'status_code' : 6001,
               'message' : 'No such user found!'
          }
          return Response(response_data)
     else:
          if Cart.objects.filter(Q(user_id = pk),Q(is_ordered=False)).exists():
               instances = Cart.objects.filter(Q(user_id=pk),Q(is_ordered=False))
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
                    'message' : 'Your Cart is Empty'
               }
               return Response(response_data)

     
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def addToCart(request):
     user_id = request.data["user_id"],
     product_id = request.data["product_id"],
     quantity = request.data["quantity"]

     item = Cart.objects.filter(Q(user_id=user_id),Q(product_id = product_id),Q(is_ordered=False) ).values('quantity')
     if item.exists():
          old_quantity = item[0].get('quantity')
          new_quantity = old_quantity + int(quantity)
          if new_quantity > 5:
               new_quantity = 5
          item.update(quantity = new_quantity)
     else:     
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


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def addToWishlist(request):
     user_id = request.data["user_id"],
     product_id = request.data["product_id"]
     
     item = Wishlist.objects.filter(Q(user_id=user_id),Q(product_id = product_id))
     if item.exists():
          response_data = {
          'status_code' : 6001,
          'message' : 'Already added to wishlist'
          }
     else:     
          Wishlist.objects.create(
               user_id = request.data["user_id"],
               product_id = request.data["product_id"]
          )
          response_data = {
               'status_code' : 6000,
               'message' : 'Item added to wishlist'
          }
     return Response(response_data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getwishlist(request,pk):
     if not(User.objects.filter(id = pk)).exists():
          response_data = {
               'status_code' : 6001,
               'message' : 'No such user found!'
          }
          return Response(response_data)
     else:
          if Wishlist.objects.filter(user_id = pk).exists():
               instances = Wishlist.objects.filter(user_id=pk)
               context = {"request" : request}
               serializer = WishlistSerializer(instances,many =True,context = context)
               response_data = {
                    'status_code' : 6000,
                    'data' : serializer.data
               }
               return Response(response_data)
          else:
               response_data = {
                    'status_code' : 6001,
                    'message' : 'Your Wishlist is Empty'
               }
               return Response(response_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def removeFromCart(request):
     user_id = request.data["user_id"]
     cart_id = request.data["cart_id"]
     if Cart.objects.filter( Q(user_id = user_id) ,Q(id = cart_id) ).exists():
          Cart.objects.filter( Q(user_id = user_id) ,Q(id = cart_id) ).delete()
          response_data = {
               'status_code' : 6000,
               'message' : 'Item deleted from cart'
          }
     else:
          response_data = {
               'status_code' : 6001,
               'message' : 'Invalid Data'
          }
     return Response(response_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def removeFromWishlist(request):
     user_id = request.data["user_id"]
     wishlist_id = request.data["wishlist_id"]
     if Wishlist.objects.filter( Q(user_id = user_id) ,Q(id = wishlist_id) ).exists():
          Wishlist.objects.filter( Q(user_id = user_id) ,Q(id = wishlist_id) ).delete()
          response_data = {
               'status_code' : 6000,
               'message' : 'Item deleted from wishlist'
          }
     else:
          response_data = {
               'status_code' : 6001,
               'message' : 'Invalid Data'
          }
     return Response(response_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def changeCartQuantity(request):
     cart_id = request.data["cart_id"]
     quantity = request.data["quantity"]
     if Cart.objects.filter(id = cart_id).exists():
          Cart.objects.filter(id = cart_id).update(quantity = quantity)
          response_data = {
               'status_code' : 6000,
               'message' : 'Quantity changed'
          }
     else:
          response_data = {
               'status_code' : 6001,
               'message' : 'Cart not exist'
          }
     return Response(response_data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getOrders(request,pk):
     if not(User.objects.filter(id = pk)).exists():
          response_data = {
               'status_code' : 6001,
               'message' : 'No such user found!'
          }        
     else:
          if Order.objects.filter(user = pk).exists():
               instances = Order.objects.filter(user = pk)
               context = {"request" : request}
               serializer = OrderSerializer(instances,many=True,context = context)
               response_data = {
                    'status_code' : 6000,
                    'data' : serializer.data
               }              
          else:
               response_data = {
                    'status_code' : 6001,
                    'message' : 'Your Order List is Empty'
               }
     return Response(response_data)


@api_view(["GET"])
@permission_classes([AllowAny])
def banners(request):
     instances = Banner.objects.all()
     context = {"request" : request}
     serializer = BannerSerializer(instances,many =True,context = context)
     response_data = {
          'status_code' : 6000,
          'data' : serializer.data
     }
     return Response(response_data)