from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

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

def home(request):
    context = {
        'items' : Item.objects.all()
    }
    return render(request, "home-page.html", context)