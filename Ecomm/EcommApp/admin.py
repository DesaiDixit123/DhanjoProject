from django.contrib import admin
from .models.user import User
from .models.category import Category
from .models.product import Product
from .models.cart import Cart,CartItem
from .models.checkout import ShippingAddress,Order,OrderItem,Payment,Chckout
# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Chckout)
