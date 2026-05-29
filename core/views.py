from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from shop.models import Product
from .models import Review, FAQCategory

def home(request):
    new_products = Product.objects.filter(available=True).order_by('-id')[:10]
    latest_reviews = Review.objects.all()[:10]
    
    return render(request, 'core/home.html', {
        'new_products': new_products,
        'latest_reviews': latest_reviews,
    })

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        if first_name and last_name and email and message:
            admin_subject = f"New Contact Request from {first_name} {last_name}"
            admin_html_message = render_to_string('emails/contact_notification.html', {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'message': message,
            })
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

            user_subject = "Thank you for contacting Bongs Luxury Glass"
            user_html_message = render_to_string('emails/contact_confirmation.html', {
                'first_name': first_name,
            })
            user_plain_message = strip_tags(user_html_message)
            try:
                send_mail(
                    user_subject,
                    user_plain_message,
                    settings.EMAIL_HOST_USER,
                    [email],
                    html_message=user_html_message,
                    fail_silently=True,
                )
            except Exception:
                pass

            messages.success(request, "Your message has been sent successfully!")
            return redirect('core:contact')
        else:
            messages.error(request, "Please fill in all fields.")
            
    return render(request, 'core/contact.html')

def faq(request):
    faq_categories = FAQCategory.objects.prefetch_related('faqs').all()
    return render(request, 'core/faq.html', {'faq_categories': faq_categories})

def reviews(request):
    reviews_list = Review.objects.all()
    return render(request, 'core/reviews.html', {'reviews': reviews_list})
