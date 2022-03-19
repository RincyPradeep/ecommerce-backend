from django.contrib import admin
from web.models import Product,Category,Cart
 
 
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","image","title","price","is_available","is_featured"]
 
admin.site.register(Product,ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
    
admin.site.register(Category,CategoryAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ["id","user_id","product_id","quantity"]
    
admin.site.register(Cart,CartAdmin)