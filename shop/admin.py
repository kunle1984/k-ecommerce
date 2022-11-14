
from django.contrib import admin
from .models import MyUser, Product,Category,Brand, Order

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Order)
