from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category

# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryId = request.GET.get('category')
    if categoryId:
        products = Product.get_all_products_by_categoryid(categoryId)
    else:
        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)

def signup(request):
    return render(request, 'signup.html')