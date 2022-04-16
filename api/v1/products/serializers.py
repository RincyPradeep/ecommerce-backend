from rest_framework.serializers import ModelSerializer
 
from products.models import Product,Category,Cart,Order,Banner,Wishlist
from rest_framework import serializers
 
  
class ProductSerializer(ModelSerializer):
    category = serializers.SerializerMethodField()
 
    class Meta:
        model = Product
        fields = ('id','title','image','description','price','category','is_available','added_at','is_featured')
 
    def get_category(self,instance):
        return instance.category.name


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id','user','product','is_ordered','quantity')


class WishlistSerializer(ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ('id','user','product')


class OrderSerializer(ModelSerializer):
    order_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model = Order
        fields = ('id','order_payment_id','order_date','product_title','product_id','product_amount','quantity','order_amount','isPaid','status')


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = ('id','image')