from django.contrib import admin
from .models import Category, Product, ProductImage, ProductReview


def get_ancestor_categories(category):
    """Walk up the tree and collect this category + all its ancestors."""
    cats = []
    current = category
    while current:
        cats.append(current)
        current = current.parent
    return cats


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

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        product = form.instance

        # Auto-assign ancestors for every selected category so you only
        # need to pick the leaf (e.g. "Beakers") and the system silently
        # adds "Bongs" and "Smoking" for correct filtering on parent pages.
        ancestors_to_add = []
        for cat in list(product.categories.all()):
            for ancestor in get_ancestor_categories(cat):
                if ancestor not in ancestors_to_add:
                    ancestors_to_add.append(ancestor)
        if ancestors_to_add:
            product.categories.add(*ancestors_to_add)

        # Auto-assign artist/studio categories from the artists text field
        self._auto_assign_artist_categories(product)

    def _auto_assign_artist_categories(self, product):
        """
        For each name in the artists field, find any Category whose name
        matches (case-insensitive) and automatically assign that category
        AND all of its ancestors to the product.
        e.g. artists="Sovereignty" → assigns Sovereignty → Studios → All Creators
        Supports comma-separated values: "Sovereignty, Toro"
        """
        if not product.artists:
            return

        artist_names = [a.strip() for a in product.artists.split(',') if a.strip()]
        cats_to_add = []

        for name in artist_names:
            matched = Category.objects.filter(name__iexact=name)
            for cat in matched:
                cats_to_add.extend(get_ancestor_categories(cat))

        if cats_to_add:
            product.categories.add(*cats_to_add)

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'created']
    list_filter = ['rating', 'created']
