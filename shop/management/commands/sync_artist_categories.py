"""
Management command to retroactively assign creator categories
to existing products based on their artists field.

Usage:
    python manage.py sync_artist_categories
    python manage.py sync_artist_categories --dry-run
"""
from django.core.management.base import BaseCommand
from shop.models import Category, Product


def get_ancestor_categories(category):
    cats = []
    current = category
    while current:
        cats.append(current)
        current = current.parent
    return cats


class Command(BaseCommand):
    help = 'Auto-assign creator categories to products based on their artists field'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be changed without making changes',
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        updated = 0

        products = Product.objects.prefetch_related('categories').all()

        for product in products:
            cats_to_add = []

            # 1. Ancestors for every category already on the product
            for cat in product.categories.all():
                for ancestor in get_ancestor_categories(cat):
                    if ancestor not in cats_to_add:
                        cats_to_add.append(ancestor)

            # 2. Artist categories from the artists text field
            if product.artists:
                artist_names = [a.strip() for a in product.artists.split(',') if a.strip()]
                for name in artist_names:
                    matched = Category.objects.filter(name__iexact=name)
                    for cat in matched:
                        for ancestor in get_ancestor_categories(cat):
                            if ancestor not in cats_to_add:
                                cats_to_add.append(ancestor)

            if cats_to_add:
                existing = set(product.categories.all())
                new_cats = [c for c in cats_to_add if c not in existing]
                if new_cats:
                    cat_names = ', '.join(c.name for c in new_cats)
                    self.stdout.write(f"  [{product.name}] -> adding: {cat_names}")
                    if not dry_run:
                        product.categories.add(*new_cats)
                    updated += 1

        action = 'Would update' if dry_run else 'Updated'
        self.stdout.write(self.style.SUCCESS(f'\n{action} {updated} products.'))
