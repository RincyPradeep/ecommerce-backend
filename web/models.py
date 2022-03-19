from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator


class Product(models.Model):
    image = models.ImageField(upload_to="products/")
    title = models.CharField(max_length=128)
    description = models.TextField()
    category = models.ForeignKey("web.Category",on_delete=models.CASCADE)
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
        db_table = "web_category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name 


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey("web.Product",on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    def __str__(self):
        return str(self.id)
