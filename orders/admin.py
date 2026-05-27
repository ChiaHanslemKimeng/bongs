from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import Order, OrderItem, Coupon

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.payment_instructions and not obj.payment_instructions_sent:
            user_subject = f"Payment Instructions for Order #{obj.id}"
            user_html_message = render_to_string('emails/payment_instructions.html', {'order': obj})
            user_plain_message = strip_tags(user_html_message)
            try:
                send_mail(
                    user_subject,
                    user_plain_message,
                    settings.EMAIL_HOST_USER,
                    [obj.email],
                    html_message=user_html_message,
                    fail_silently=True,
                )
                obj.payment_instructions_sent = True
                obj.save(update_fields=['payment_instructions_sent'])
            except Exception:
                pass

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']
    search_fields = ['code']
