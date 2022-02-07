from django.shortcuts import render, redirect
from store.models import Product, Category
from django.views import View

# Create your views here.

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity+1
            else:
                cart[product] = 1

        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('homepage')

    def get(self, request):
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
        print(request.session.get('email'))
        return render(request, 'index.html', data)
