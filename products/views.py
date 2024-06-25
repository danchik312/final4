# products/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Slogan, YouTubeVideo, Product, Review

def home(request):
    slogan = Slogan.objects.first()
    video = YouTubeVideo.objects.first()
    top_gadgets = Product.objects.order_by('-popularity')[:5]
    return render(request, 'products/home.html', {
        'slogan': slogan,
        'video': video,
        'top_gadgets': top_gadgets
    })

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    reviews = product.reviews.all()
    return render(request, 'products/product_detail.html', {'product': product, 'reviews': reviews})

def add_review(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Review.objects.create(product=product, content=content)
        return redirect('product_detail', id=product.id)
    return render(request, 'products/add_review.html', {'product': product})
