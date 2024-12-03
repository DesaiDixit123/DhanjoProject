from EcommApp.models.category import Category
from django.shortcuts import render

def Category_List(request):
    print("Category_List view has been called.")  # Debug message
    categories = Category.get_all_categories()
    print("Categories from the database:", categories)
    return render(request, 'products.html', {'categories': categories})
