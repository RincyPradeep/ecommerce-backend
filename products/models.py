from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


ORDER_STATUS = (
    ("Ordered","Ordered"),
    ("Shipped","Shipped"),
    ("Delivered","Delivered"),
    ("pending","Pending")   
)

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    address = models.TextField()
    pincode = models.IntegerField()
    mobile = models.BigIntegerField()

    def __str__(self):
        return self.user 


class Product(models.Model):
    image = models.ImageField(upload_to="products/")
    title = models.CharField(max_length=128)
    description = models.TextField()
    category = models.ForeignKey("products.Category",on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    is_available = models.BooleanField(default = True)
    added_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default = False)
    is_deleted = models.BooleanField(default = False)
 
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = "product_category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name 


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["-id"]

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["-id"]


class Order(models.Model):
    user = models.IntegerField()
    name = models.CharField(max_length=25)
    address = models.TextField()
    pincode = models.IntegerField()
    mobile = models.BigIntegerField()
    email = models.EmailField()
    order_amount = models.FloatField(max_length=25)
    product_title = models.CharField(max_length=250)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    product_amount = models.FloatField(max_length=25)
    order_payment_id = models.CharField(max_length=100)
    isPaid = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length = 25, default = "Pending",choices=ORDER_STATUS)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering =["-order_date"]


class Banner(models.Model):
    image = models.ImageField(upload_to="banners/")
    
    def __str__(self):
        return str(self.id)