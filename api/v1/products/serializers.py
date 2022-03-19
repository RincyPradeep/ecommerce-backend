from rest_framework.serializers import ModelSerializer
 
from web.models import Product,Category,Cart
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
        fields = ('id','user_id','product_id','quantity')