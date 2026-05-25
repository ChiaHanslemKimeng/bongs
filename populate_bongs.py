import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

def populate():
    from shop.models import Category, Product, ProductImage
    from django.core.files import File

    # Clear existing
    Category.objects.all().delete()
    Product.objects.all().delete()

    # Create categories
    cats = {
        'beakers': Category.objects.create(name='Beaker Bongs', slug='beaker-bongs', description='Classic, stable, and highly functional.'),
        'tubes': Category.objects.create(name='Straight Tubes', slug='straight-tubes', description='Direct hit, easy to clear, sleek design.'),
        'rigs': Category.objects.create(name='Dab Rigs', slug='dab-rigs', description='Smaller, flavor-focused pieces for concentrates.')
    }

    # Create products
    products = [
        # Beaker Bongs
        {'cat': cats['beakers'], 'name': 'Classic 12" Beaker', 'slug': 'classic-12-beaker', 'price': '89.99', 'stock': 50, 'description': 'Our classic 12-inch heavy-wall beaker. Features an ice pinch and comes with a 14mm bowl and diffused downstem.', 'is_trending': True, 'is_bestseller': False},
        {'cat': cats['beakers'], 'name': '18" Tall Beaker with Perc', 'slug': '18-tall-beaker-perc', 'price': '149.99', 'stock': 20, 'description': 'Towering 18-inch beaker featuring a 6-arm tree percolator for extra filtration.', 'is_trending': False, 'is_bestseller': True},
        {'cat': cats['beakers'], 'name': 'Halo Ring Beaker', 'slug': 'halo-ring-beaker', 'price': '109.99', 'stock': 30, 'description': 'A stunning 14-inch beaker featuring an ice-notch halo collar and double-thick joints for robust durability.', 'is_trending': True, 'is_bestseller': False},
        {'cat': cats['beakers'], 'name': 'Mini Beaker Bubbler', 'slug': 'mini-beaker-bubbler', 'price': '59.99', 'stock': 40, 'description': 'A travel-friendly 8-inch beaker that packs a heavy punch. Features a fixed showerhead downstem.', 'is_trending': False, 'is_bestseller': False},
        {'cat': cats['beakers'], 'name': 'UFO Perc Beaker', 'slug': 'ufo-perc-beaker', 'price': '135.00', 'stock': 15, 'description': 'A 16-inch beaker with a built-in UFO percolator in the mid-section for double cooling and smooth diffusion.', 'is_trending': False, 'is_bestseller': False},
        {'cat': cats['beakers'], 'name': 'Artisan Fumed Beaker', 'slug': 'artisan-fumed-beaker', 'price': '199.99', 'stock': 8, 'description': 'Hand-blown fumed borosilicate beaker that changes color dynamically when in use. Every piece is unique.', 'is_trending': False, 'is_bestseller': True},
        {'cat': cats['beakers'], 'name': 'Frostline Beaker', 'slug': 'frostline-beaker', 'price': '115.00', 'stock': 25, 'description': '15-inch beaker bong with a frosted glass neck and a black glass base for an exquisite, clean styling.', 'is_trending': True, 'is_bestseller': False},
        
        # Straight Tubes
        {'cat': cats['tubes'], 'name': 'Honeycomb Straight Tube', 'slug': 'honeycomb-straight-tube', 'price': '119.99', 'stock': 35, 'description': 'Sleek 14-inch straight tube with a double honeycomb percolator for incredible stacking bubbles.', 'is_trending': False, 'is_bestseller': True},
        {'cat': cats['tubes'], 'name': 'Inline Perc Tube', 'slug': 'inline-perc-tube', 'price': '129.99', 'stock': 15, 'description': 'Stemless design straight tube with a gridded inline percolator. Super smooth pull.', 'is_trending': True, 'is_bestseller': False},
        {'cat': cats['tubes'], 'name': 'Tree Perc Straight Tube', 'slug': 'tree-perc-straight-tube', 'price': '99.99', 'stock': 30, 'description': 'Classic 14-inch straight tube with a 4-arm tree perc for extra smooth diffusion and minimal drag.', 'is_trending': False, 'is_bestseller': False},
        {'cat': cats['tubes'], 'name': 'Double Showerhead Tube', 'slug': 'double-showerhead-tube', 'price': '155.00', 'stock': 12, 'description': '16-inch straight tube stacked with two layers of showerhead percolators for the ultimate filtration.', 'is_trending': False, 'is_bestseller': True},
        {'cat': cats['tubes'], 'name': 'Gridline Straight Tube', 'slug': 'gridline-straight-tube', 'price': '145.00', 'stock': 18, 'description': 'Stemless straight tube featuring a precision-cut gridline percolator for zero drag and maximum airflow.', 'is_trending': True, 'is_bestseller': False},
        {'cat': cats['tubes'], 'name': 'Slimline Micro Tube', 'slug': 'slimline-micro-tube', 'price': '65.00', 'stock': 20, 'description': 'An elegant 10-inch micro straight tube with a single disc perc. Great for small spaces and quick sessions.', 'is_trending': False, 'is_bestseller': False},
        {'cat': cats['tubes'], 'name': 'Quantum Ring Tube', 'slug': 'quantum-ring-tube', 'price': '125.00', 'stock': 22, 'description': 'A thick 15-inch straight tube with circular ice pinches and a color-matching base ring.', 'is_trending': False, 'is_bestseller': False},

        # Dab Rigs
        {'cat': cats['rigs'], 'name': 'Mini Matrix Rig', 'slug': 'mini-matrix-rig', 'price': '95.00', 'stock': 40, 'description': 'Compact 7-inch rig featuring a 360-degree matrix percolator. Perfect flavor saver.', 'is_trending': True, 'is_bestseller': False},
        {'cat': cats['rigs'], 'name': 'Tornado Recycler', 'slug': 'tornado-recycler', 'price': '185.00', 'stock': 10, 'description': 'Mesmerizing recycler rig that continuously spins your water and vapor for the coolest hit possible.', 'is_trending': True, 'is_bestseller': True},
        {'cat': cats['rigs'], 'name': 'Showerhead Mini Rig', 'slug': 'showerhead-mini-rig', 'price': '79.99', 'stock': 28, 'description': '6-inch ultra-portable rig with a high-flow showerhead perc. Retains maximum terpene profile.', 'is_trending': False, 'is_bestseller': False},
        {'cat': cats['rigs'], 'name': 'Double Recycler Rig', 'slug': 'double-recycler-rig', 'price': '210.00', 'stock': 6, 'description': 'Premium 9-inch recycler that continuously cycles water to filter vapor and eliminate splashback.', 'is_trending': False, 'is_bestseller': True},
        {'cat': cats['rigs'], 'name': 'Klein Recycler', 'slug': 'klein-recycler', 'price': '195.00', 'stock': 9, 'description': 'Beautifully sculpted Klein design that redirects water internally to save space while maximizing action.', 'is_trending': True, 'is_bestseller': False},
        {'cat': cats['rigs'], 'name': 'Micro Matrix Rig', 'slug': 'micro-matrix-rig-new', 'price': '85.00', 'stock': 15, 'description': 'An even more compact 5-inch dab rig with a micro matrix core designed for flavor connoisseurs.', 'is_trending': False, 'is_bestseller': False},
        {'cat': cats['rigs'], 'name': 'Incubator Rig', 'slug': 'incubator-rig', 'price': '165.00', 'stock': 14, 'description': 'Features an inner sphere chamber that houses the percolator, separating bubbles from the splash guard.', 'is_trending': False, 'is_bestseller': False}
    ]

    from django.core.files import File
    import os
    
    # Exact mapping of slug to image filename
    image_map = {
        'classic-12-beaker': 'classic_12_beaker.png',
        '18-tall-beaker-perc': 'tall_beaker_perc.png',
        'honeycomb-straight-tube': 'honeycomb_straight_tube.png',
        'inline-perc-tube': 'inline_perc_tube.png',
        'mini-matrix-rig': 'mini_matrix_rig.png',
        'tornado-recycler': 'tornado_recycler.png',
        
        # New Beaker Bongs
        'halo-ring-beaker': 'beaker_bong.png',
        'mini-beaker-bubbler': 'tall_beaker_perc.png',
        'ufo-perc-beaker': 'classic_12_beaker.png',
        'artisan-fumed-beaker': 'beaker_bong.png',
        'frostline-beaker': 'classic_12_beaker.png',
        
        # New Straight Tubes
        'tree-perc-straight-tube': 'straight_tube.png',
        'double-showerhead-tube': 'honeycomb_straight_tube.png',
        'gridline-straight-tube': 'inline_perc_tube.png',
        'slimline-micro-tube': 'straight_tube.png',
        'quantum-ring-tube': 'inline_perc_tube.png',
        
        # New Dab Rigs
        'showerhead-mini-rig': 'dab_rig.png',
        'double-recycler-rig': 'tornado_recycler.png',
        'klein-recycler': 'tornado_recycler.png',
        'micro-matrix-rig-new': 'mini_matrix_rig.png',
        'incubator-rig': 'dab_rig.png',
    }

    images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'images')
    
    for p_data in products:
        product, created = Product.objects.get_or_create(
            category=p_data['cat'],
            slug=p_data['slug'],
            defaults={
                'name': p_data['name'],
                'price': p_data['price'],
                'stock': p_data['stock'],
                'description': p_data['description'],
                'available': True,
                'is_trending': p_data['is_trending'],
                'is_bestseller': p_data['is_bestseller']
            }
        )
        
        # Attach the exact product image
        image_name = image_map.get(product.slug)
        if image_name:
            image_path = os.path.join(images_dir, image_name)
            if os.path.exists(image_path):
                with open(image_path, 'rb') as f:
                    product.image.save(image_name, File(f), save=True)
                    
        # Add gallery images (reuse other generic images for the gallery)
        generic_images = ['beaker_bong.png', 'dab_rig.png', 'straight_tube.png']
        for i, g_img in enumerate(generic_images):
            g_path = os.path.join(images_dir, g_img)
            if os.path.exists(g_path):
                with open(g_path, 'rb') as f:
                    gallery_img = ProductImage(product=product)
                    gallery_img.image.save(f"{product.slug}_gallery_{i}.png", File(f), save=True)

    print("Database populated with Bong products successfully!")

if __name__ == '__main__':
    populate()
