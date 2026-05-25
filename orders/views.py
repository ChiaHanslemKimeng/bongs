from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .models import OrderItem, Order

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity)
    # Using HTMX, we can return the updated cart icon HTML, but for simplicity we redirect
    return redirect('orders:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('orders:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'orders/cart.html', {'cart': cart})

def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        # Here we would handle Stripe checkout
        # For now, create the order directly
        order = Order.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            postal_code=request.POST.get('postal_code'),
            city=request.POST.get('city'),
        )
        if request.user.is_authenticated:
            order.user = request.user
            order.save()
            
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()
        return render(request, 'orders/created.html', {'order': order})
        
    return render(request, 'orders/checkout.html', {'cart': cart})
