from django.urls import path
from api.v1.products import views
 
 
urlpatterns = [
    path('',views.products),
    path('singleproduct/<int:pk>/',views.singleProduct),
    path('categories/',views.categories),
    path('category-products/<int:pk>/',views.category_products),
    path('search/',views.search),
    path('cart/<int:pk>/',views.getcart),
    path('wishlist/<int:pk>/',views.getwishlist),
    path('addtocart/',views.addToCart),
    path('addtowishlist/',views.addToWishlist),
    path('removefromcart/',views.removeFromCart),
    path('removefromwishlist/',views.removeFromWishlist),
    path('changecartquantity/',views.changeCartQuantity),
    path('orders/<int:pk>/',views.getOrders),
    path('banners/',views.banners)
]
