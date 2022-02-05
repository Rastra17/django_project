from django.shortcuts import render, redirect
from .models import Product, Category, Customer
from django.contrib.auth.hashers import make_password, check_password

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
    if request.method=='GET':
        return render(request, 'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        #Validation

        value = {
            'first_name' : first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
        }

        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        if (not first_name):
            error_message = "First Name Required !!"
        elif len(first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not last_name:
            error_message = 'Last Name Required'
        elif len(last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not phone:
            error_message = 'Phone Number required'
        elif len(phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email address already exists'

        #Saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values' : value
            }
            return render(request, 'signup.html', data)