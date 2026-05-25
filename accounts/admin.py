from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Unregister unused allauth / auth tables
try:
    from allauth.account.models import EmailAddress
    admin.site.unregister(EmailAddress)
except Exception:
    pass

try:
    from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken
    admin.site.unregister(SocialApp)
    admin.site.unregister(SocialAccount)
    admin.site.unregister(SocialToken)
except Exception:
    pass

try:
    from django.contrib.auth.models import Group
    admin.site.unregister(Group)
except Exception:
    pass

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('phone_number', 'address')}),
    )
