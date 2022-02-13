from django.shortcuts import render
from store.models.product import Product

def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        productSearch = Product.objects.filter(name__contains=searched)
        return render(request,
                      'search.html',
                      {'searched': searched,
                       'productSearch': productSearch})
    else:
        return render(request, 'search.html')
