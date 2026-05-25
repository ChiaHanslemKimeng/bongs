import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from blog.models import Post
from accounts.models import User
from django.utils.text import slugify

def populate():
    Post.objects.all().delete()

    user, created = User.objects.get_or_create(email='author@bongs.luxury', defaults={
        'username': 'Elias Vance',
        'is_staff': True,
        'is_superuser': True
    })
    if created:
        user.set_password('password')
        user.save()

    blogs_data = [
        ("The Science of Percolation: Why Bubbles Matter", "Percolation is the heart of a smooth hit. When smoke travels through a water pipe, percolators break it down into thousands of tiny bubbles. This drastically increases the surface area of the smoke coming into contact with the water, which cools the vapor and filters out water-soluble particulates. The result? A remarkably clean, terpene-rich draw that preserves the delicate flavors of your flower while protecting your throat from harsh heat.\n\nThere are many types of percolators — inline, tree, matrix, honeycomb, and showerhead — each offering a slightly different experience. Honeycomb percs, for instance, are prized for their near-zero drag and exceptional diffusion. Matrix percs produce an incredibly even bubble spread. Understanding the differences is the first step to choosing the perfect bong for your needs."),
        ("Borosilicate Glass: The Unsung Hero of Luxury Pipes", "Not all glass is created equal. While many cheap imported pipes use 'soft glass' or soda-lime mixtures, premium bongs are exclusively crafted from heavy-wall borosilicate. Originally developed for laboratory environments (and famously used in early Pyrex), borosilicate glass has a very low coefficient of thermal expansion. This means it can withstand rapid temperature changes — like adding ice to a hot piece — without cracking under stress.\n\nThe difference is immediately tangible. Pick up a borosilicate bong and a soda-lime one side by side. The weight, the clarity, the way it rings when tapped — everything speaks to a higher standard. At BONGS, we use only 5mm+ wall thickness for all our standard pieces, and 7mm for our premium collection."),
        ("Anatomy of a Dab Rig", "Dab rigs are specialized water pipes designed specifically for vaporizing concentrates. Unlike traditional bongs, rigs are typically smaller. This is intentional: less air volume inside the chamber means less time for the vapor to cool and condense on the glass walls, preserving the potency and flavor of the concentrate.\n\nRecycler rigs take this a step further by constantly cycling water and vapor through multiple chambers, ensuring maximum filtration with minimum drag. The key components of any rig are the joint, the banger (the bucket-shaped heating element that replaces a bowl), the downstem, and the water chamber. High-quality quartz bangers are the gold standard, offering superior thermal retention and zero flavor contamination."),
        ("How to Properly Clean Your Glass", "Nothing ruins the aesthetic of a luxury glass piece quite like resin buildup. The secret to pristine glass isn't harsh chemicals; it's high-percentage isopropyl alcohol (91% or higher) and coarse salt. The alcohol acts as a solvent to break down the sticky resin, while the salt acts as an abrasive scrubber that won't scratch your borosilicate glass.\n\nFor a deep clean: pour a generous amount of iso and a tablespoon of coarse salt into the bong. Cover all openings with your hands or plugs, then shake vigorously for 60 seconds. Rinse thoroughly with warm water. For stubborn spots on the downstem or percolator, let the piece soak in iso for 30 minutes before shaking. A weekly routine will keep your piece looking showroom-ready."),
        ("The Evolution of the Beaker Bong", "The beaker bong is perhaps the most iconic silhouette in smoking culture, borrowing its design directly from the Erlenmeyer flasks used in chemistry labs. This wide, flat base serves two critical functions: it holds a massive volume of water for superior filtration, and it lowers the center of gravity, making the piece incredibly stable and resistant to tipping over.\n\nOver the decades, glassblowers have pushed the beaker form into new artistic territory. Modern beakers feature ice pinches molded directly into the neck, fixed downstems with integrated diffusers, and even multi-chamber systems where a secondary beaker sits above the main one. It's a perfect marriage of scientific function and timeless form."),
        ("Straight Tubes vs. Beakers: Which is Right for You?", "Choosing between a straight tube and a beaker base often comes down to personal preference in 'pull' style. Straight tubes offer a very direct, fast-clearing hit. The smoke travels linearly, meaning less lung capacity is required to clear the chamber. Beakers, with their voluminous bases, allow you to milk a massive hit before pulling the slide, delivering a much larger, denser volume of smoke at once.\n\nFor beginners or those who prefer a lighter, more controlled session, a straight tube is usually the better choice. For experienced smokers who want a full, satisfying cloud, a beaker's volume is unmatched. Many collectors own both — a straight tube for everyday use and a beaker for when the occasion calls for something special."),
        ("Understanding Joint Sizes and Genders", "Navigating joint sizes can be confusing for newcomers. The industry standards are 10mm, 14mm, and 18mm. Most modern flower bongs use a 14mm female joint (requiring a 14mm male bowl). Larger, high-airflow pieces might use an 18mm joint, while dedicated concentrate rigs frequently use 10mm or 14mm joints.\n\nThe 'gender' of a joint refers to its shape: female joints are open at the top to receive a male accessory, while male joints have a protruding stub. Always ensure your downstems, bowls, and ash catchers match both the size and the opposite gender of your bong's joint. Buying an adapter is always an option, but starting with compatible accessories is always cleaner."),
        ("The Art of American Lampworking", "Lampworking, or flameworking, is a specialized type of glassblowing where a torch is used to melt the glass. In the United States, a counter-culture movement in the late 20th century transformed lampworking from a utilitarian craft into a legitimate fine art form. Today, master glassblowers spend years perfecting techniques like fuming (vaporizing precious metals like gold and silver onto the glass), producing functional art that appreciates in value.\n\nThe Pacific Northwest — particularly Oregon and Washington — became the epicenter of American glass art in the 1990s. Artists like Bob Snodgrass pioneered color-changing fumed glass techniques that launched an entire aesthetic movement. At BONGS, our lead artist Elias Vance trained under third-generation lampworkers from this tradition, bringing that heritage to every piece we produce."),
        ("Why Ash Catchers Are Essential Upgrades", "An ash catcher is a modular accessory that fits between your bowl and your bong's joint. Its primary purpose is right in the name: it catches ash and resin before it can enter the main chamber of your bong. This keeps your expensive, complex percolators clean for much longer.\n\nAdditionally, many ash catchers feature their own built-in percolators, adding an extra layer of filtration to your setup. A honeycomb ash catcher, for example, can turn a simple beaker into a double-perc system without buying a new bong entirely. When choosing an ash catcher, ensure its joint angle matches your bong's (typically 45° or 90°), and that the joint sizes are compatible."),
        ("Temperature Control: The Key to Flavor", "Whether you are combusting flower or vaporizing concentrates, temperature is the ultimate variable dictating your experience. Lighting flower with hemp wick instead of a butane lighter provides a lower-temperature cherry, preserving volatile terpenes. For dabbing, utilizing a quartz banger with a carb cap and a thermometer allows you to vaporize at exactly the right temperature (usually between 450°F and 550°F), unlocking the full flavor profile of the extract.\n\nLow-temperature dabs (below 500°F) are increasingly popular among flavor connoisseurs. At lower temps, the more volatile and aromatic terpenes survive the vaporization process, producing a lighter, more nuanced taste. The trade-off is slightly less visible vapor. High-temp dabs (above 600°F) produce thick, immediate clouds but sacrifice much of the flavor complexity."),
        ("Building Your First High-End Glass Collection", "Starting a glass collection is a deeply personal journey. Our recommendation for a first serious piece is always a mid-size beaker bong in the 12-to-14 inch range with a fixed downstem and a simple diffuser. This gives you the most versatile experience: easy to clean, great filtration, and stable enough for daily use.\n\nFrom there, consider branching into a dedicated dab rig. A compact recycler in borosilicate with a 14mm or 10mm female joint pairs perfectly with a high-quality quartz banger. Finally, an ash catcher adds years to the life of both pieces. A collection of three or four well-chosen pieces will serve you better than a shelf full of cheap glass that constantly needs replacing."),
        ("The Hidden World of Limited Edition Glass Art", "Beyond functional bongs lies a rarefied world of limited-edition glass art, where collectors pay thousands of dollars for a single piece that will never be smoked. These art pieces push the boundaries of lampworking technique: sculptural designs embedded inside the glass, impossibly thin walls decorated with precious metal fuming, and forms that challenge any conventional notion of what a bong can look like.\n\nArtists like Banjo, Salt, and Sovereignty Glass command cult followings and secondary market premiums that rival fine art. At BONGS, we collaborate with emerging artists to produce small, numbered runs of functional art pieces — items that are equally at home in a gallery display case or at the center of a luxury smoking session. Sign up for our newsletter to be notified of the next drop."),
    ]

    base_date = datetime.now() - timedelta(days=36)

    from django.core.files import File
    import os
    
    posts = []
    for title, content in blogs_data:
        posts.append({
            'title': title,
            'slug': slugify(title),
            'content': content
        })

    images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'images')
    # Use an explicit list of exactly 12 unique premium glass images
    blog_images = [
        'about_detail.jpg', 'studio_glass.png', 'tornado_recycler.png', 'hero4.jpg',
        'classic_12_beaker.png', 'tall_beaker_perc.png', 'honeycomb_straight_tube.png', 'story.jpg',
        'hero3.jpg', 'bong_hero.png', 'about_hero.jpg', 'studio_artist.png'
    ]

    for i, p_data in enumerate(posts):
        post, created = Post.objects.get_or_create(
            slug=p_data['slug'],
            defaults={
                'title': p_data['title'],
                'author': user,
                'body': p_data['content'],
                'status': 'published'
            }
        )
        
        # Pop unique image based on index
        if i < len(blog_images):
            img_name = blog_images[i]
            img_path = os.path.join(images_dir, img_name)
            if os.path.exists(img_path):
                with open(img_path, 'rb') as f:
                    post.image.save(img_name, File(f), save=True)
                
        post.save()

    print(f"Successfully populated {len(blogs_data)} blogs.")

if __name__ == '__main__':
    populate()
