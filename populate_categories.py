import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from shop.models import Category

hierarchy = {
    "All Creators": {
        "Studios": ["Sovereignty", "Toro", "Swiss Perc", "Illadelph", "Mothership", "Mobius"],
        "Established Artists": ["Elbo", "Slinger", "Darby Holm", "Bear Mountain Studios", "Lyons"],
        "Emerging Artists": ["LX1984", "DarkeVitrum", "OJ Flame", "Jarred Bennett", "Fire Within Glass", "HotHead Glass"],
        "Brands": ["Puffco", "Moodmats", "Dab Rite", "Storz & Bickel", "Stündenglass", "Highly Educated"]
    },
    "Smoking": {
        "Bongs": ["Beakers", "Straight Tubes", "Heady Bongs($1k+)"],
        "Bubblers": ["Push Bubblers($1k+)"],
        "Dry Pipes": ["Spoons", "Sherlocks", "Chillums", "Hammer Pipes", "Heady Pipes($1k+)"],
        "Accessories": ["Ash Catchers", "Dry Catchers", "Slides", "Adapters", "Downstems"]
    },
    "Dabbing": {
        "Rigs": ["Recyclers", "Heady Rigs", "Banger Hangers"],
        "Puffco": ["Peak Pro Glass Tops", "Puffco Accessories", "Proxy Attachments", "Puffco Carb Caps"],
        "Bangers": ["Slurpers", "Under $50", "Under $100", "Under $200"],
        "Essentials": ["Baller Jars", "Dab Stations", "Adapters", "Temperature Devices"]
    },
    "Glass Accessories": {
        "Smoking": ["Slides", "Downstems", "Adapters", "Ash Catchers", "Dry Catchers", "Pokers"],
        "Dabbing": ["Carb Caps", "Dab Tools", "Slurper Sets", "Torches", "Temperature Devices"],
        "Non-Functional Glass": ["Pendants", "Marbles", "Jars", "Beads", "Glassware"],
        "General": ["Bags & Cases", "Mats & Pads", "Grinders", "Slide Stands", "Rolling Trays", "Ash Trays"]
    },
    "Lifestyle": {
        "Apparel": ["T-Shirts", "Hoodies", "Hats", "Shorts", "GlassPass Merch"],
        "Collectibles": ["Moodmats", "Plushies", "Original Artwork & Prints", "Stickers", "Vinyl Toys"],
        "Miscellaneous": ["Cleaning Supplies", "Events (coming soon!)", "Community (coming soon!)"]
    }
}

def create_categories(data, parent=None):
    if isinstance(data, dict):
        for key, value in data.items():
            slug = slugify(key)
            base_slug = slug
            counter = 1
            while Category.objects.filter(slug=slug).exclude(name=key, parent=parent).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
                
            category, created = Category.objects.get_or_create(
                name=key,
                parent=parent,
                defaults={'slug': slug}
            )
            create_categories(value, category)
    elif isinstance(data, list):
        for item in data:
            slug = slugify(item)
            base_slug = slug
            counter = 1
            while Category.objects.filter(slug=slug).exclude(name=item, parent=parent).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            Category.objects.get_or_create(
                name=item,
                parent=parent,
                defaults={'slug': slug}
            )

if __name__ == '__main__':
    print("Populating categories...")
    # First clear old categories if user wants a clean slate, but let's just add to avoid deleting existing products
    # Products might lose their category if we delete. Let's just create.
    create_categories(hierarchy)
    print("Done!")
