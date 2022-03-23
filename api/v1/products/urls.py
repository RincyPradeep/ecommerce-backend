from django.urls import path
from api.v1.products import views
 
 
urlpatterns = [
    path('',views.products),
    path('singleproduct/<int:pk>/',views.singleProduct),
    path('categories/',views.categories),
    path('cart/<int:pk>/',views.getcart),
    path('addtocart/',views.addToCart),
    path('removefromcart/',views.removeFromCart),
    path('changecartquantity/',views.changeCartQuantity)
]
