from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Product

def get_category_descendants(category):
    descendants = [category]
    for child in category.children.all():
        descendants.extend(get_category_descendants(child))
    return descendants

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(parent__isnull=True)
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        descendant_categories = get_category_descendants(category)
        products = products.filter(categories__in=descendant_categories).distinct()
        
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(name__icontains=search_query)
        
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    if min_price:
        try:
            products = products.filter(price__gte=min_price)
        except ValueError:
            pass
            
    if max_price:
        try:
            products = products.filter(price__lte=max_price)
        except ValueError:
            pass

    # Pill Filters
    if request.GET.get('american') == 'true':
        products = products.filter(is_american=True)
    if request.GET.get('artists') == 'true':
        products = products.filter(is_artist_piece=True)
    if request.GET.get('auctions') == 'true':
        products = products.filter(is_auction=True)
    if request.GET.get('new') == 'true':
        products = products.filter(is_new_drop=True)
            
    # Sorting
    sort_by = request.GET.get('sort', 'recent')
    if sort_by == 'price_asc':
        products = products.order_by('price')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')
    elif sort_by == 'popular':
        products = products.order_by('-is_trending', '-created')
    elif sort_by == 'auction':
        # Placeholder for auction sorting, fallback to recent
        products = products.order_by('-created')
    else: # most recent or relevant
        products = products.order_by('-created')

    # Breadcrumbs
    breadcrumbs = []
    curr = category
    while curr:
        breadcrumbs.insert(0, curr)
        curr = curr.parent

    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
            
    return render(request, 'shop/product_list.html', {
        'category': category,
        'categories': categories,
        'products': page_obj,
        'page_obj': page_obj,
        'min_price': min_price,
        'max_price': max_price,
        'sort_by': sort_by,
        'breadcrumbs': breadcrumbs,
        'total_listings': paginator.count,
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    related_products = Product.objects.filter(categories__in=product.categories.all(), available=True).exclude(id=product.id).distinct()[:4]
    
    return render(request, 'shop/product_detail.html', {
        'product': product,
        'related_products': related_products
    })
