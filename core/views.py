from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Item, OrderItem, Order

# Create your views here.

def products(request):
    context = {
        'items' : Item.objects.all()
    }
    return render(request, "product-page.html", context)

def checkout(request):
    return render(request, "checkout-page.html")

class HomeView(ListView):
    model = Item
    template_name = "home-page.html"

class ItemDetailView(DetailView):
    model = Item
    template_name = "product-page.html"
    
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item = OrderItem.objects.create(item=item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # Check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exist():
            order_item.quantity += 1
            order_item.save()