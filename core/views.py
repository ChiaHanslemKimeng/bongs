from django.shortcuts import render
from shop.models import Product
from .models import Review
from blog.models import Post

def home(request):
    # Get trending and bestseller products for the hero section
    trending_products = Product.objects.filter(is_trending=True, available=True)[:4]
    bestsellers = Product.objects.filter(is_bestseller=True, available=True)[:4]
    latest_reviews = Review.objects.all()[:10]
    latest_posts = Post.objects.filter(status='published').order_by('-publish')[:3]
    
    return render(request, 'core/home.html', {
        'trending_products': trending_products,
        'bestsellers': bestsellers,
        'latest_reviews': latest_reviews,
        'latest_posts': latest_posts,
    })

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def faq(request):
    return render(request, 'core/faq.html')

def reviews(request):
    reviews_list = Review.objects.all()
    return render(request, 'core/reviews.html', {'reviews': reviews_list})
