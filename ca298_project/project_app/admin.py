from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Basket)
admin.site.register(BasketItems)
admin.site.register(Vegetable)
