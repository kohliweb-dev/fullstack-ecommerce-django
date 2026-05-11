from django.db import models
from category.models import Category
from django.urls import reverse

    
class Gender(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name    

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    contant = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.FloatField(default=0)
    stoke = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/') 
  

    def get_url(self):
        return reverse('product_details',args = [self.category.slug,self.slug,self.gender.slug])
     
    def __str__(self):
        return str(self.title)
    
    


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
 
    def __str__(self):
            return str(self.product.title)
    
    
# ⭐ NEW MODEL (important)
class ShoeSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sizes')
    
    SIZE_CHOICES = [
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]

    size = models.CharField(max_length=5, choices=SIZE_CHOICES)
    stock = models.IntegerField()

    def __str__(self):
         return f"{str(self.product.title)} - Size {self.size}"


class Banner(models.Model):
    PAGE_CHOICES=(
        ('home','Home page'),
        ('about','About page'),
        ('products','Products page')
    )
    contact = models.TextField()
    title= models.CharField(max_length=255)
    page = models.CharField(max_length=20, choices=PAGE_CHOICES)
    image = models.ImageField(upload_to= 'banner/') 
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return f"{self.title} - {self.page}"  
    

class offers(models.Model):
    text = models.CharField(max_length=225)
    is_active = models.BooleanField(default=True)    

    def __str__(self):
        return self.text

