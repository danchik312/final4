from django.shortcuts import render
from .models import Slogan, YouTubeVideo, Product

def home(request):
    slogan = Slogan.objects.first()
    video = YouTubeVideo.objects.first()
    top_products = Product.objects.order_by('-id')[:5]
    context = {
        'slogan': slogan,
        'video': video,
        'top_products': top_products,
    }
    return render(request, 'home.html', context)

def products_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products_list.html', context)

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    reviews = product.reviews.all()
    context = {
        'product': product,
        'reviews': reviews,
    }
    return render(request, 'product_detail.html', context)
