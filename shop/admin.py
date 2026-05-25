from django.contrib import admin
from .models import Category, Product, ProductImage, ProductReview

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'is_trending', 'is_bestseller', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'is_trending', 'is_bestseller', 'category']
    list_editable = ['price', 'stock', 'available', 'is_trending', 'is_bestseller']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'created']
    list_filter = ['rating', 'created']
