from django.shortcuts import render,redirect
from EcommApp.models.category import Category
from EcommApp.models.product import Product
from django.views import View
from EcommApp.views.cart_utils import get_or_create_cart


class Index(View):
    
    
    def get(self,request):
        all_products = Product.objects.all()
        categories = Category.get_all_categories()
        return render(request,"index.html", {'products': all_products,'categories': categories})
    
    
    
    
    
    
    
    
    
def store(request):
    products = None
    categories = Category.get_all_categories() 
    category_id = request.GET.get('category')  

    if category_id:
        products = Product.get_all_products_by_categories_id(category_id)
    else:
        products = Product.get_all_products()

    data = {
        'products': products,
        'categories': categories
    }

    print('You are:', request.session.get('email'))  # Debug statement for session check
    print('Products:', products)
    print('Categories:', categories)
    
    return render(request, "products.html", data)


