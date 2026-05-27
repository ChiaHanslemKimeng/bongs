from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from shop.models import Product
from .cart import Cart
from .models import OrderItem, Order

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity)
    return redirect('orders:cart_detail')

@require_POST
def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity, override_quantity=True)
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
        order = Order.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            postal_code=request.POST.get('postal_code'),
            city=request.POST.get('city'),
            payment_method=request.POST.get('payment_method', 'Credit Card'),
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
        
        # Send confirmation email to User
        user_subject = f"Order Confirmation #{order.id}"
        user_html_message = render_to_string('emails/order_confirmation.html', {'order': order})
        user_plain_message = strip_tags(user_html_message)
        try:
            send_mail(
                user_subject,
                user_plain_message,
                settings.EMAIL_HOST_USER,
                [order.email],
                html_message=user_html_message,
                fail_silently=True,
            )
        except Exception:
            pass

        # Send notification email to Admin
        admin_subject = f"New Order Received #{order.id}"
        admin_html_message = render_to_string('emails/order_notification.html', {'order': order})
        admin_plain_message = strip_tags(admin_html_message)
        admin_email = getattr(settings, 'ADMIN_EMAIL', getattr(settings, 'EMAIL_HOST_USER', ''))
        if admin_email:
            try:
                send_mail(
                    admin_subject,
                    admin_plain_message,
                    settings.EMAIL_HOST_USER,
                    [admin_email],
                    html_message=admin_html_message,
                    fail_silently=True,
                )
            except Exception:
                pass
                
        return render(request, 'orders/created.html', {'order': order})
        
    return render(request, 'orders/checkout.html', {'cart': cart})
