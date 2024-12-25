from django.shortcuts import render
from .urls import *
from product.models import Product,ReviewRating

def home(request):
    products = Product.objects.all()
    
    # get the reviews
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    
    context = {
        'products':products,
        'reviews':reviews,
    }
    return render(request, 'home.html', context)