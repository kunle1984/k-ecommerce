
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):

    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    address = models.TextField(null=True)
    image = models.ImageField(null=True)
    mobile_number = models.CharField(max_length=10, blank=True, null=True)
    address=models.TextField()
    country=models.CharField(max_length=200, null=True, blank=True)
    state=models.CharField(max_length=200, null=True, blank=True)
    postcode=models.CharField(max_length=200, null=True, blank=True)
    city=models.CharField(max_length=200, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



class Brand(models.Model):
    name=models.CharField(max_length=200, null=True)
    image=models.ImageField(upload_to="brand_images")
    def __str__(self):
        return self.name
class Category(models.Model):
    name=models.CharField(max_length=200, null=True)
    image=models.ImageField(upload_to="category_images")
    def __str__(self):
        return self.name

class Product(models.Model):
    user=models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length=200, null=True)
    price=models.FloatField(null=True, blank=True)
    discount_price=models.FloatField(null=True, blank=True)
    category=models.ForeignKey(Category,  on_delete=models.CASCADE, null=True, blank=True)
    brand=models.ForeignKey(Brand,  on_delete=models.CASCADE, null=True, blank=True)
    description=models.TextField()
    additional_info=models.TextField()
    shipping_info=models.TextField()
    trending_product=models.BooleanField()
    top_product=models.BooleanField()
    in_stock=models.BooleanField(default=True)
    image1=models.ImageField(upload_to="product_images")
    image2=models.ImageField(upload_to="product_images")
    image3=models.ImageField(upload_to="product_images")
    def __str__(self):
        return self.title



class Order(models.Model):
    user=models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    order_number=models.CharField(max_length=50, blank=True, null=True, verbose_name="Order Track Id")
    first_name=models.CharField(max_length=200, blank=False, null=False)
    last_name=models.CharField(max_length=200, blank=False, null=False)
    company_name=models.CharField(max_length=200, blank=True, null=True)
    country=models.CharField(max_length=200, blank=False, null=False)
    city=models.CharField(max_length=200, blank=False, null=False)
    phone=models.CharField(max_length=200, blank=False, null=False)
    address=models.CharField(max_length=500)
    email=models.EmailField(max_length=200, blank=False, null=False)
    postcode=models.CharField(max_length=200)
    create=models.DateTimeField(auto_now_add=True)
    note=models.TextField()
    order=models.CharField(max_length=1000)
    has_paid=models.BooleanField(default=False, verbose_name="Payment status")
    stripe_payment_intent = models.CharField( max_length=200)
    amount=models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} -{self.city}'



