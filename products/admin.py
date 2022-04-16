from django.contrib import admin
from products.models import Profile,Product,Category,Cart,Order,Banner,Wishlist
 
 
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id","user","address","pincode","mobile"]
 
admin.site.register(Profile,ProfileAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","image","title","price","is_available","is_featured"]
 
admin.site.register(Product,ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
    
admin.site.register(Category,CategoryAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ["id","user","product","quantity","is_ordered"]
    
admin.site.register(Cart,CartAdmin)

class WishlistAdmin(admin.ModelAdmin):
    list_display = ["id","user","product"]
    
admin.site.register(Wishlist,WishlistAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id","order_date","name","address","pincode","mobile","email","product_title","quantity","order_amount","order_payment_id","isPaid","status"]

admin.site.register(Order,OrderAdmin)


class BannerAdmin(admin.ModelAdmin):
    list_display = ["id","image"]
    
admin.site.register(Banner,BannerAdmin)