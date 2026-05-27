"""
Comprehensive GlassPass-style product population script.
Populates every leaf category with 3-5 realistic products.
No image downloads - products are created with no image (add via admin later).
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.utils.text import slugify
from shop.models import Category, Product


def get_cat(slug):
    try:
        return Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        print(f"  !! Category not found: {slug}")
        return None


def make_product(cat_slug, name, price, description, stock=20,
                 is_trending=False, is_bestseller=False):
    cat = get_cat(cat_slug)
    if cat is None:
        return

    slug = slugify(name)
    base = slug
    n = 1
    while Product.objects.filter(slug=slug).exclude(category=cat, name=name).exists():
        slug = f"{base}-{n}"
        n += 1

    product, created = Product.objects.get_or_create(
        slug=slug,
        defaults={
            'category': cat,
            'name': name,
            'price': price,
            'description': description,
            'stock': stock,
            'available': True,
            'is_trending': is_trending,
            'is_bestseller': is_bestseller,
        }
    )
    status = "CREATED" if created else "EXISTS "
    print(f"  [{status}] {name}")


def populate():

    # ── SMOKING > Bongs > Beakers ─────────────────────────────────────────
    make_product("beakers", "Sovereignty Beaker 50x5", 399.99,
        "Classic Sovereignty 18\" beaker in 50mm diameter, 5mm glass. Ice-notch, worked logo.", is_trending=True)
    make_product("beakers", "Illadelph Heavy Hitter Beaker", 449.99,
        "Illadelph's signature heavy beaker with coloured coil for smooth hits.", is_bestseller=True)
    make_product("beakers", "Toro 7-13 Beaker", 349.99,
        "Toro's legendary two-stage 7/13 diffusion beaker. Minimal drag, maximum filtration.", is_trending=True, is_bestseller=True)
    make_product("beakers", "Swiss Perc Classic Beaker", 289.99,
        "Swiss Perc borosilicate beaker with gridded diffuser and ice catcher.")
    make_product("beakers", "Mobius 60T Beaker", 325.00,
        "Mobius 60mm tube beaker with internal showerhead downstem and polished joint.", is_bestseller=True)

    # ── SMOKING > Bongs > Straight Tubes ─────────────────────────────────
    make_product("straight-tubes", "Mothership Fab Egg Tube", 1250.00,
        "Mothership's iconic fab egg recycler tube. Truly breathtaking headwork.", is_trending=True, is_bestseller=True)
    make_product("straight-tubes", "Toro Straight 13-Arm", 525.00,
        "14-inch Toro straight tube with 13-arm tree percolator and matching bowl.", is_bestseller=True)
    make_product("straight-tubes", "Illadelph Classic Straight", 350.00,
        "Illadelph's timeless 18\" straight tube, colour-tipped with ice pinch.", is_trending=True)
    make_product("straight-tubes", "Sovereignty Standard Straight", 299.99,
        "Sovereignty 18\" straight tube in 50x5 with signature worked logo detail.")
    make_product("straight-tubes", "Mobius Ion 8-Arm Straight", 385.00,
        "Mobius Ion series 8-arm percolator straight tube in clear borosilicate.", is_bestseller=True)

    # ── SMOKING > Bongs > Heady Bongs ($1k+) ─────────────────────────────
    make_product("heady-bongs1k", "Elbo Heady Worked Beaker", 2500.00,
        "One-of-a-kind Elbo heady beaker with full worked colour and signature opals.", is_trending=True, is_bestseller=True)
    make_product("heady-bongs1k", "Slinger Signature Heady Tube", 1800.00,
        "Slinger's hand-sculpted worked tube — full colour, accented with fume.", is_trending=True)
    make_product("heady-bongs1k", "Bear Mountain Studios Monument", 3200.00,
        "Bear Mountain Studios epic heady bong with sculpted bears and forest detail.", is_bestseller=True)
    make_product("heady-bongs1k", "Lyons Puffed Heady Beaker", 1500.00,
        "Lyons' signature puffed accents on a full-worked beaker. Museum quality.")

    # ── SMOKING > Bubblers > Push Bubblers ($1k+) ────────────────────────
    make_product("push-bubblers1k", "Elbo Push Bubbler Worked", 1400.00,
        "Elbo's classic push bubbler with full colour worked chamber and opals.", is_trending=True, is_bestseller=True)
    make_product("push-bubblers1k", "Darby Holm Signature Bubbler", 1650.00,
        "Darby Holm hand-sculpted push bubbler with dichroic accents and worked stem.", is_bestseller=True)
    make_product("push-bubblers1k", "Slinger Heady Push Bubbler", 1250.00,
        "Slinger worked push bubbler — vibrant fumed colour with honey-comb mouthpiece.", is_trending=True)

    # ── SMOKING > Dry Pipes > Spoons ────────────────────────────────────
    make_product("spoons", "Fumed Classic Spoon", 45.00,
        "Hand-blown fumed borosilicate spoon pipe. Color-changing with use.", is_bestseller=True)
    make_product("spoons", "Dichroic Rainbow Spoon", 65.00,
        "Stunning dichroic glass spoon that shifts from green to gold in sunlight.", is_trending=True)
    make_product("spoons", "Marble Swirl Spoon", 55.00,
        "Unique marble swirl pattern on a deep-bowled spoon. Every piece is different.")
    make_product("spoons", "Mini Pocket Spoon", 35.00,
        "Ultra-compact 3\" spoon pipe. Perfect for on-the-go sessions.")
    make_product("spoons", "Pendant Spoon with Opal", 95.00,
        "Artisan spoon with UV-reactive opal inlay. Display-worthy piece.", is_trending=True, is_bestseller=True)

    # ── SMOKING > Dry Pipes > Sherlocks ─────────────────────────────────
    make_product("sherlocks", "Classic Borosilicate Sherlock", 75.00,
        "Full-size 6\" sherlock with a wide bowl and smooth draw.", is_bestseller=True)
    make_product("sherlocks", "Fumed Sherlock Pipe", 89.00,
        "Hand-blown fumed sherlock that shifts colour dynamically with heat.", is_trending=True)
    make_product("sherlocks", "UV-Reactive Sherlock", 110.00,
        "Glows brilliant blue under UV light. Thick borosilicate construction.", is_trending=True)
    make_product("sherlocks", "Worked Art Sherlock", 185.00,
        "Artist-made sherlock with fully worked colour and marble accents.", is_bestseller=True)

    # ── SMOKING > Dry Pipes > Chillums ──────────────────────────────────
    make_product("chillums", "Stone One-Hitter Chillum", 25.00,
        "Sleek stone chillum for quick, clean one-hitter sessions.")
    make_product("chillums", "Worked Colour Chillum", 45.00,
        "Hand-worked colour chillum with unique swirl design.", is_bestseller=True)
    make_product("chillums", "Glass Stone Chillum", 35.00,
        "Thick-walled glass chillum with a stone texture exterior.", is_trending=True)
    make_product("chillums", "UV Glow Chillum", 55.00,
        "UV-reactive chillum that glows bright green under blacklight.", is_trending=True)

    # ── SMOKING > Dry Pipes > Hammer Pipes ──────────────────────────────
    make_product("hammer-pipes", "Classic Hammer Bubbler", 85.00,
        "Traditional flat-bottomed hammer bubbler. Sits upright on any surface.", is_bestseller=True)
    make_product("hammer-pipes", "Fumed Hammer Pipe", 99.00,
        "Hand-blown fumed hammer pipe with colour-changing glass body.", is_trending=True)
    make_product("hammer-pipes", "Worked Hammer Bubbler", 145.00,
        "Fully worked hammer bubbler with swirled colour and opal inlays.")

    # ── SMOKING > Dry Pipes > Heady Pipes ($1k+) ────────────────────────
    make_product("heady-pipes1k", "LX1984 Heady Worked Pipe", 1100.00,
        "LX1984's signature worked pipe with full colour and CFL reactive accents.", is_trending=True)
    make_product("heady-pipes1k", "OJ Flame Signature Spoon", 1350.00,
        "OJ Flame's iconic heady spoon with worked accents and deep, sculpted bowl.", is_bestseller=True)
    make_product("heady-pipes1k", "Fire Within Glass Art Pipe", 1200.00,
        "Fire Within Glass full worked art pipe. Stunning display piece that smokes perfectly.", is_trending=True, is_bestseller=True)

    # ── SMOKING > Accessories ────────────────────────────────────────────
    make_product("slides", "14mm Worked Colour Slide", 35.00,
        "Hand-blown 14mm slide with worked colour accents and clear handle.", is_bestseller=True)
    make_product("slides", "18mm Clear Slide Bowl", 29.00,
        "Classic clear borosilicate 18mm slide bowl with deep funnel shape.")
    make_product("downstems", "14mm to 18mm Diffused Downstem", 25.00,
        "High-quality 6-slot diffused downstem. Available in 3\", 4\", 5\" lengths.", is_bestseller=True)
    make_product("downstems", "Gridded Inline Downstem", 39.00,
        "Gridded inline diffuser downstem for maximum diffusion and smooth draws.", is_trending=True)
    make_product("adapters", "14mm to 18mm Glass Adapter", 18.00,
        "Convert your 14mm joint to 18mm or vice versa. Male-to-female.")
    make_product("ash-catchers", "45 Degree Ash Catcher with Perc", 55.00,
        "14mm ash catcher with built-in showerhead perc to keep your bong clean.", is_trending=True, is_bestseller=True)
    make_product("dry-catchers", "Dry Ash Catcher 90 Degree", 42.00,
        "90-degree dry ash catcher to prevent ash from entering your main piece.")

    # ── DABBING > Rigs > Recyclers ───────────────────────────────────────
    make_product("recyclers", "Toro Micro Circ Recycler", 795.00,
        "Toro's legendary micro circ recycler. Perfect function meets perfect form.", is_trending=True, is_bestseller=True)
    make_product("recyclers", "Mothership Klein Recycler", 1800.00,
        "Mothership's famous Klein recycler. Silky smooth with zero splashback.", is_trending=True, is_bestseller=True)
    make_product("recyclers", "Sovereignty Recycler Rig", 450.00,
        "Sovereignty's 7\" recycler with inline to showerhead diffusion.", is_bestseller=True)
    make_product("recyclers", "Compact 4 Inch Recycler Rig", 185.00,
        "Compact 4-inch recycler with external tube for continuous water cycle.", is_trending=True)
    make_product("recyclers", "Double Uptake Recycler", 265.00,
        "Dual uptake tubes feed a swirling internal chamber for maximum cooling.")

    # ── DABBING > Rigs > Heady Rigs ─────────────────────────────────────
    make_product("heady-rigs", "Elbo Signature Heady Rig", 2800.00,
        "Elbo's masterpiece heady rig — fully worked with dichroic glass and opals.", is_trending=True, is_bestseller=True)
    make_product("heady-rigs", "DarkeVitrum Sculpted Rig", 1950.00,
        "DarkeVitrum's hand-sculpted heady rig with layered worked glass chambers.", is_bestseller=True)
    make_product("heady-rigs", "HotHead Glass Heady Rig", 1500.00,
        "HotHead Glass signature piece — vivid wig-wag and full colour worked body.", is_trending=True)
    make_product("heady-rigs", "Jarred Bennett Heady Rig", 2200.00,
        "Jarred Bennett one-of-a-kind heady rig. Signed and numbered.", is_bestseller=True)

    # ── DABBING > Rigs > Banger Hangers ─────────────────────────────────
    make_product("banger-hangers", "Clear Banger Hanger Mini Rig", 95.00,
        "Simple 5\" banger hanger rig with a 45-degree angled joint. Great starter rig.", is_bestseller=True)
    make_product("banger-hangers", "Colour-Accent Banger Hanger", 145.00,
        "Banger hanger with worked colour accents and matching carb cap.", is_trending=True)
    make_product("banger-hangers", "Swiss Perc Banger Hanger", 235.00,
        "Swiss Perc's signature swiss-hole banger hanger for pure, flavourful draws.", is_bestseller=True)
    make_product("banger-hangers", "Sovereignty Banger Hanger", 310.00,
        "Sovereignty banger hanger with inline perc and signature worked logo.", is_trending=True, is_bestseller=True)

    # ── DABBING > Puffco > Peak Pro Glass Tops ──────────────────────────
    make_product("peak-pro-glass-tops", "Puffco Peak Pro Standard Glass Top", 79.99,
        "Original Puffco Peak Pro glass top. Borosilicate, fits all Peak Pro models.", is_bestseller=True)
    make_product("peak-pro-glass-tops", "Puffco Peak Pro XL Glass Top", 99.99,
        "Extended XL glass top for bigger hits on the Puffco Peak Pro.", is_trending=True)
    make_product("peak-pro-glass-tops", "Peak Pro Coloured Replacement Top", 89.99,
        "Coloured borosilicate replacement top for the Puffco Peak Pro.")

    # ── DABBING > Puffco > Puffco Accessories ────────────────────────────
    make_product("puffco-accessories", "Puffco Peak Pro Travel Pack", 69.99,
        "Includes protective case, USB-C cable and extra carb cap.", is_bestseller=True)
    make_product("puffco-accessories", "Puffco Atomizer Replacement", 59.99,
        "OEM replacement 3D chamber atomizer for Puffco Peak Pro.", is_trending=True, is_bestseller=True)
    make_product("puffco-accessories", "Puffco Loading Tool", 14.99,
        "Official Puffco silicone loading tool for mess-free concentrate loading.")

    # ── DABBING > Puffco > Proxy Attachments ────────────────────────────
    make_product("proxy-attachments", "Puffco Proxy Base Station", 49.99,
        "Desktop base station for the Puffco Proxy — keeps it upright and charged.")
    make_product("proxy-attachments", "Proxy Pipe Attachment", 89.99,
        "Unique pipe-style glass attachment for the Puffco Proxy.", is_trending=True)
    make_product("proxy-attachments", "Proxy Volcano Bubbler Attachment", 129.99,
        "Bubbler-style glass attachment for the Puffco Proxy with water filtration.", is_bestseller=True)

    # ── DABBING > Puffco > Puffco Carb Caps ─────────────────────────────
    make_product("puffco-carb-caps", "Puffco Directional Carb Cap", 29.99,
        "Directional airflow carb cap compatible with all Puffco bangers.", is_bestseller=True)
    make_product("puffco-carb-caps", "Spinner Carb Cap for Puffco", 39.99,
        "Terp pearl spinning carb cap for the Puffco Peak Pro.", is_trending=True)

    # ── DABBING > Bangers > Slurpers ────────────────────────────────────
    make_product("slurpers", "Flat-Top Slurper Banger 14mm", 65.00,
        "Quartz flat-top slurper with side holes and dish. Perfect terp pearl action.", is_trending=True, is_bestseller=True)
    make_product("slurpers", "Thermal Slurper Banger", 85.00,
        "Thermal double-wall slurper banger for extended heat retention.", is_bestseller=True)
    make_product("slurpers", "Castle Slurper with Dish", 95.00,
        "Castle-top slurper with matching quartz dish and two terp pearls.", is_trending=True)

    # ── DABBING > Bangers > Under $50 ───────────────────────────────────
    make_product("under-50", "Basic Flat-Top Banger 14mm", 28.00,
        "Clean quartz flat-top banger, 2mm wall, 14mm male. Great daily driver.", is_bestseller=True)
    make_product("under-50", "Bevelled-Edge Banger", 35.00,
        "Precision-cut bevelled edge banger for perfect carb cap sealing.")
    make_product("under-50", "Terp Slurper Value Banger", 45.00,
        "Entry-level terp slurper banger with included dish. Best value.", is_trending=True, is_bestseller=True)

    # ── DABBING > Bangers > Under $100 ──────────────────────────────────
    make_product("under-100", "Opaque Quartz Banger", 75.00,
        "Opaque quartz banger for slower, more even heat-up and retention.", is_bestseller=True)
    make_product("under-100", "Ruby Insert Flat-Top Banger", 89.00,
        "Flat-top banger with a genuine ruby insert for ultimate heat retention.", is_trending=True)

    # ── DABBING > Bangers > Under $200 ──────────────────────────────────
    make_product("under-200", "Highly Educated Ti-Grade Banger", 149.00,
        "Highly Educated titanium-grade quartz banger. The benchmark.", is_bestseller=True)
    make_product("under-200", "Full-Weld Banger 4mm Wall", 175.00,
        "4mm full-weld quartz banger with integrated heat shield.", is_trending=True, is_bestseller=True)

    # ── DABBING > Essentials ─────────────────────────────────────────────
    make_product("baller-jars", "Mini Quartz Baller Jar", 25.00,
        "Quartz baller jar to store and load concentrates directly into your banger.", is_bestseller=True)
    make_product("baller-jars", "Terp Baller Set 3-Pack", 45.00,
        "Three 6mm quartz terp balls for use in slurpers and flat-top bangers.", is_trending=True)
    make_product("dab-stations", "Bamboo Dab Station", 55.00,
        "Handcrafted bamboo dab station with slots for rig, banger, pearls and tools.", is_bestseller=True)
    make_product("dab-stations", "Silicone Dab Station Tray", 35.00,
        "Non-stick silicone dab station tray with reclaim cup and tool holder.", is_trending=True)
    make_product("adapters", "18mm to 14mm Recessed Adapter", 22.00,
        "Recessed 18mm female to 14mm male adapter for dab rigs.")
    make_product("temperature-devices", "Dab Rite Digital Thermometer", 149.99,
        "Dab Rite infrared thermometer for laser-accurate banger temperature readings.", is_trending=True, is_bestseller=True)
    make_product("temperature-devices", "TerpTimer Cold Start Device", 89.99,
        "Digital timer with thermocouple sensor for repeatable cold-start dabs.", is_bestseller=True)

    # ── GLASS ACCESSORIES > Dabbing ──────────────────────────────────────
    make_product("carb-caps", "UFO Directional Carb Cap", 22.00,
        "UFO-style carb cap with directional airflow hole for terp pearls.", is_trending=True, is_bestseller=True)
    make_product("carb-caps", "Bubble Carb Cap Clear", 18.00,
        "Simple clear bubble carb cap, universal fit for flat-top bangers.", is_bestseller=True)
    make_product("dab-tools", "Titanium Dab Tool Set 3pc", 35.00,
        "Three-piece titanium dab tool set: scoop, paddle, and pick.", is_bestseller=True)
    make_product("dab-tools", "Quartz Dab Tool", 28.00,
        "All-quartz dab tool for pure, flavour-neutral concentrate handling.", is_trending=True)
    make_product("slurper-sets", "Terp Slurper Full Set", 110.00,
        "Complete slurper set: slurper banger, marbled dish, pill and two pearls.", is_trending=True, is_bestseller=True)
    make_product("slurper-sets", "Marble Slurper Set", 125.00,
        "Premium marble-style terp slurper set with matching coloured pearls.", is_bestseller=True)
    make_product("torches", "Blazer Big Shot Torch", 79.99,
        "The Blazer Big Shot butane torch. The industry standard for dabbing.", is_trending=True, is_bestseller=True)
    make_product("torches", "Newport Zero Torch", 49.99,
        "Newport Zero-Gravity butane torch. Works at any angle.", is_bestseller=True)
    make_product("temperature-devices", "Terpometer v2", 109.99,
        "Highly accurate quartz thermometer probe for banger temperature.", is_trending=True, is_bestseller=True)

    # ── GLASS ACCESSORIES > Smoking ──────────────────────────────────────
    make_product("pokers", "Titanium Poker Tool", 18.00,
        "Grade 2 titanium poker for packing bowls and prodding ash.", is_bestseller=True)
    make_product("pokers", "Glass Poker with Opal Handle", 32.00,
        "Borosilicate glass poker with UV reactive opal accent handle.", is_trending=True)

    # ── GLASS ACCESSORIES > Non-Functional Glass ─────────────────────────
    make_product("pendants", "Worked Glass Pendant", 85.00,
        "Hand-blown borosilicate pendant. Wearable art from top glassblowers.", is_trending=True)
    make_product("pendants", "UV Reactive Glass Pendant", 95.00,
        "UV reactive glass pendant that glows brilliant green under blacklight.", is_bestseller=True)
    make_product("marbles", "Colour Marble 25mm", 35.00,
        "25mm hand-blown colour glass marble. Unique swirl pattern per piece.", is_trending=True, is_bestseller=True)
    make_product("marbles", "Dichroic Marble Set 3pc", 95.00,
        "Three dichroic glass marbles that shift colour from gold to purple.", is_bestseller=True)
    make_product("jars", "Borosilicate Storage Jar 50ml", 29.00,
        "50ml wide-mouth borosilicate jar for concentrate storage.")
    make_product("jars", "Hand-Blown Art Glass Jar", 55.00,
        "Hand-blown worked glass jar with matching lid. Display and storage.", is_trending=True)
    make_product("beads", "Terp Bead Set 6mm Quartz 10pc", 22.00,
        "10-piece set of 6mm quartz terp beads for slurpers and bangers.", is_bestseller=True)
    make_product("glassware", "Custom Borosilicate Mug", 45.00,
        "Hand-blown borosilicate glass mug with worked colour handle.", is_trending=True)

    # ── GLASS ACCESSORIES > General ──────────────────────────────────────
    make_product("bags-cases", "Padded Hard-Shell Case 14 inch", 65.00,
        "Padded EVA hard-shell case fits most 14-inch bongs. Lock-and-key closures.", is_bestseller=True)
    make_product("bags-cases", "Smell-Proof Soft Carry Bag", 39.99,
        "Activated carbon smell-proof bag with combination lock zip.", is_trending=True)
    make_product("mats-pads", "Moodmats Large Dab Pad 16 inch", 29.99,
        "Moodmats silicone dab pad in 16-inch large format. Non-stick and easy clean.", is_trending=True, is_bestseller=True)
    make_product("mats-pads", "Moodmats Mini Dab Mat", 14.99,
        "Mini Moodmats silicone dab mat. Perfect for rig protection.", is_bestseller=True)
    make_product("grinders", "Titanium 4-Piece Grinder 63mm", 55.00,
        "Anodised titanium 4-piece grinder with kief catcher and pollen press.", is_trending=True)
    make_product("grinders", "Santa Cruz Shredder 3-Piece", 49.99,
        "Santa Cruz Shredder medium 3-piece grinder. Industry-standard quality.", is_bestseller=True)
    make_product("slide-stands", "Glass Slide Display Stand", 12.00,
        "Adjustable acrylic stand to display your favourite slides upright.")
    make_product("rolling-trays", "Metal Rolling Tray Large", 22.00,
        "Large magnetic metal rolling tray with high edges to prevent spillage.", is_bestseller=True)
    make_product("ash-trays", "Borosilicate Glass Ash Tray", 28.00,
        "Thick borosilicate glass ashtray with deep bowl and four rests.", is_trending=True)

    # ── LIFESTYLE > Apparel ──────────────────────────────────────────────
    make_product("t-shirts", "BONGS Classic Logo Tee", 35.00,
        "Premium cotton BONGS. logo t-shirt. Soft, relaxed fit.", is_trending=True, is_bestseller=True)
    make_product("t-shirts", "GlassPass Artist Series Tee", 42.00,
        "Limited-run GlassPass artist collab t-shirt. 100% organic cotton.", is_bestseller=True)
    make_product("hoodies", "BONGS Heavyweight Hoodie", 75.00,
        "Heavyweight 400gsm fleece hoodie with embroidered BONGS. logo.", is_trending=True)
    make_product("hoodies", "GlassPass Zip-Up Hoodie", 85.00,
        "Full-zip fleece hoodie with large front pocket and woven label.", is_bestseller=True)
    make_product("hats", "BONGS Snapback Cap", 35.00,
        "Structured snapback with embroidered BONGS. logo. One size fits most.", is_trending=True)
    make_product("hats", "GlassPass Dad Hat", 28.00,
        "Unstructured cotton dad hat with tone-on-tone embroidered logo.", is_bestseller=True)
    make_product("shorts", "BONGS Fleece Shorts", 45.00,
        "Relaxed fit fleece shorts with elastic waist and brand embroidery.")
    make_product("glasspass-merch", "GlassPass Enamel Pin Set", 18.00,
        "Set of 4 hard enamel collector pins. Exclusive GlassPass merch.", is_trending=True, is_bestseller=True)

    # ── LIFESTYLE > Collectibles ─────────────────────────────────────────
    make_product("moodmats", "Moodmats Limited Collab Mat", 39.99,
        "Limited Moodmats x GlassPass collaboration silicone dab mat.", is_trending=True, is_bestseller=True)
    make_product("plushies", "Glass Bong Plushie 12 inch", 25.00,
        "Adorable soft plushie bong. Collector item for glass enthusiasts.", is_bestseller=True)
    make_product("original-artwork-prints", "Elbo Art Print 18x24", 95.00,
        "Museum-quality Giclee art print of Elbo's signature heady designs.", is_trending=True)
    make_product("original-artwork-prints", "GlassPass Digital Art Print", 65.00,
        "Limited-edition digital art print. Signed and numbered 1/50.", is_bestseller=True)
    make_product("stickers", "GlassPass Sticker Pack 10pc", 12.00,
        "10-piece premium vinyl sticker pack. Weather and UV resistant.", is_trending=True, is_bestseller=True)
    make_product("stickers", "Artist Series Sticker Sheet", 9.00,
        "Full A4 sticker sheet featuring collab artist designs.", is_bestseller=True)
    make_product("vinyl-toys", "Glass Bong Vinyl Figure 6 inch", 55.00,
        "Limited-edition vinyl art figure styled as a worked glass bong.", is_trending=True)

    # ── LIFESTYLE > Miscellaneous ────────────────────────────────────────
    make_product("cleaning-supplies", "Formula 420 Cleaner 12oz", 18.99,
        "Instant bong cleaner. No scrubbing required. Safe on borosilicate.", is_bestseller=True)
    make_product("cleaning-supplies", "Plugs and Caps Cleaning Kit", 14.99,
        "Silicone caps and plugs to seal joints while cleaning your piece.", is_trending=True)
    make_product("cleaning-supplies", "ISO 99 Percent Isopropyl 500ml", 9.99,
        "Pharmaceutical-grade 99% isopropyl alcohol for cleaning glass.")

    # ── ALL CREATORS > Studios ───────────────────────────────────────────
    make_product("sovereignty", "Sovereignty Egg Perc Tube", 485.00,
        "Sovereignty 7\" egg perc tube with worked logo. Limited production.", is_trending=True, is_bestseller=True)
    make_product("toro", "Toro Circ to Circ 7-13", 850.00,
        "Toro's best-selling circ to circ in the 7/13 configuration.", is_trending=True, is_bestseller=True)
    make_product("swiss-perc", "Swiss Perc Gridded Inline Rig", 375.00,
        "Swiss Perc's signature gridded inline to swiss-hole chamber rig.", is_bestseller=True)
    make_product("illadelph", "Illadelph Premium Coil Bong", 520.00,
        "Illadelph coil bong with glycerin-filled coil for icy smooth hits.", is_trending=True)
    make_product("mothership", "Mothership Stereo Matrix Bong", 2200.00,
        "Mothership stereo matrix bong. Industry-defining piece.", is_trending=True, is_bestseller=True)
    make_product("mobius", "Mobius Stereo Matrix Bong", 750.00,
        "Mobius Stereo Matrix 65T. Dual matrix perc. Silky draw.", is_bestseller=True)

    # ── ALL CREATORS > Established Artists ──────────────────────────────
    make_product("elbo", "Elbo Worked Beaker 2026", 3500.00,
        "Elbo's 2026 signature worked beaker. Full colour, signed on base.", is_trending=True, is_bestseller=True)
    make_product("slinger", "Slinger Wig-Wag Tube", 1950.00,
        "Slinger full wig-wag patterned straight tube. One of a kind.", is_bestseller=True)
    make_product("darby-holm", "Darby Holm Collab Rig", 2100.00,
        "Darby Holm sculpted rig — organic form with worked colour.", is_trending=True)
    make_product("bear-mountain-studios", "Bear Mountain Totem Bong", 2800.00,
        "Bear Mountain Studios totem-inspired heady bong. Award-winning work.", is_bestseller=True)
    make_product("lyons", "Lyons Worked Spoon", 895.00,
        "Lyons hand-worked spoon with signature puffed accents and opals.", is_trending=True, is_bestseller=True)

    # ── ALL CREATORS > Emerging Artists ─────────────────────────────────
    make_product("lx1984", "LX1984 CFL Reactive Rig", 750.00,
        "LX1984 CFL-reactive heady rig. Shifts colour under daylight vs CFL.", is_trending=True, is_bestseller=True)
    make_product("darkevitrum", "DarkeVitrum Worked Pendant", 320.00,
        "DarkeVitrum fully worked pendant with wig-wag and opal detail.", is_bestseller=True)
    make_product("oj-flame", "OJ Flame Signature Spoon 2026", 1100.00,
        "OJ Flame's 2026 signature spoon. Deep sculpted bowl with worked accents.", is_trending=True)
    make_product("jarred-bennett", "Jarred Bennett Heady Rig", 1800.00,
        "Jarred Bennett heady rig. Signed and dated. Emerging artist pick.", is_bestseller=True)
    make_product("fire-within-glass", "Fire Within Glass Art Tube", 980.00,
        "Fire Within Glass full worked tube. Vivid colours, masterful technique.", is_trending=True, is_bestseller=True)
    make_product("hothead-glass", "HotHead Glass Mini Heady", 650.00,
        "HotHead Glass compact heady rig. Big personality in a small package.", is_bestseller=True)

    # ── ALL CREATORS > Brands ────────────────────────────────────────────
    make_product("puffco", "Puffco Peak Pro Smart Rig", 399.99,
        "Puffco Peak Pro — the world's most advanced electronic dab rig.", is_trending=True, is_bestseller=True)
    make_product("moodmats", "Moodmats Collector Edition Pack", 49.99,
        "Three-mat Moodmats collector pack in exclusive colourways.", is_bestseller=True)
    make_product("dab-rite", "Dab Rite Infrared Thermometer", 149.99,
        "Dab Rite — the definitive banger temperature reading device.", is_trending=True, is_bestseller=True)
    make_product("storz-bickel", "Storz and Bickel Mighty Plus Vaporizer", 399.00,
        "Storz & Bickel Mighty+ portable vaporizer. Medical-grade efficiency.", is_bestseller=True)
    make_product("stundenglass", "Stundenglass Gravity Infuser", 599.99,
        "Stundenglass gravity bong infuser. NASA-inspired kinetic technology.", is_trending=True, is_bestseller=True)
    make_product("highly-educated", "Highly Educated V3 Ti Banger", 175.00,
        "Highly Educated V3 titanium-grade quartz banger. The gold standard.", is_bestseller=True)

    print("\nDone! All GlassPass-style products created successfully.")


if __name__ == '__main__':
    print("Populating GlassPass-style products (no image downloads)...\n")
    populate()
