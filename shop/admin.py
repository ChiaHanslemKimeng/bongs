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
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'is_trending', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'is_trending', 'categories']
    list_editable = ['price', 'stock', 'available', 'is_trending']
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('categories',)
    inlines = [ProductImageInline]
    ordering = ['-created']

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'categories', 'image', 'description', 'price')
        }),
        ('Inventory & Status', {
            'fields': ('available', 'stock', 'is_trending', 'is_deal', 'is_american', 'is_artist_piece', 'is_auction', 'is_new_drop')
        }),
        ('Product Details', {
            'fields': ('artists', 'model_name', 'condition', 'color', 'color_type', 'origin', 'joint', 'year_made')
        }),
    )

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'created']
    list_filter = ['rating', 'created']
