from django.contrib import admin
from .models import Review, FAQCategory, FAQ

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')

class FAQInline(admin.TabularInline):
    model = FAQ
    extra = 1

@admin.register(FAQCategory)
class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    inlines = [FAQInline]

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'order')
    list_filter = ('category',)
