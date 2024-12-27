from django.shortcuts import render
from .urls import *
from product.models import Product,ReviewRating
from .models import Banners,SmallBanners

def home(request):
    banners = None
    products = Product.objects.all()
    
    # get the reviews
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
        
    # get banners
    banners = Banners.objects.all()
    for banner in banners:
        images = Banners.objects.all()
        
    smallbanners = SmallBanners.objects.all()
    
    context = {
        'products':products,
        'reviews':reviews,
        'images'  :images,
        'smallbanners':smallbanners,
    }
    return render(request, 'home.html', context)