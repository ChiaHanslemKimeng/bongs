import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import FAQCategory, FAQ

# Clear existing
FAQ.objects.all().delete()
FAQCategory.objects.all().delete()

# Create categories and FAQs
cats = [
    {
        'name': 'Ordering & Payments',
        'order': 1,
        'faqs': [
            ('How do I place an order?', 'Simply browse our shop, add items to your cart, and proceed to checkout. Fill in your shipping details, select your preferred payment method, and submit your order. You will receive an email confirmation with your order details.'),
            ('What payment methods do you accept?', 'We accept Credit Card, PayPal, and Cryptocurrency payments. After placing your order, our team will send you specific payment instructions based on the method you selected.'),
            ('Can I modify or cancel my order?', 'You can request modifications or cancellations within 2 hours of placing your order by contacting us via our Contact page or replying to your order confirmation email. Once an order has been packed or shipped, it cannot be cancelled.'),
            ('How will I receive my payment instructions?', 'After you place an order, our admin team will review it and send you a professional email with detailed payment instructions specific to your chosen payment method. Please check your inbox and spam folder.'),
            ('Is my payment information secure?', 'Absolutely. We never store your payment details on our servers. All transactions are processed through secure, encrypted channels to ensure your financial information remains protected.'),
        ]
    },
    {
        'name': 'Shipping & Delivery',
        'order': 2,
        'faqs': [
            ('Do you ship internationally?', 'Yes! We ship worldwide. Shipping costs and delivery times vary depending on your location. Free shipping is available on orders over $150 within the continental United States.'),
            ('How long does shipping take?', 'Domestic orders typically arrive within 3-7 business days. International orders may take 7-21 business days depending on the destination and customs processing. Expedited shipping options are available at checkout.'),
            ('How are products packaged?', 'Every piece is individually wrapped in thick bubble wrap, nestled inside custom-cut foam inserts, and placed in double-walled corrugated boxes. We take extreme care to ensure your glass arrives in perfect condition.'),
            ('Can I track my order?', 'Yes. Once your order has shipped, you will receive a tracking number via email. You can use this to monitor your package in real-time through the carrier\'s website.'),
            ('What if my order arrives damaged?', 'In the rare event that your item arrives damaged, please contact us within 48 hours of delivery with photos of the damage. We will arrange a replacement or full refund at no extra cost to you.'),
        ]
    },
    {
        'name': 'Product Information',
        'order': 3,
        'faqs': [
            ('What type of glass do you use?', 'All of our pieces are crafted from premium borosilicate glass (commonly known by the brand name Pyrex). This scientific-grade glass offers superior thermal shock resistance, durability, and clarity compared to standard soft glass.'),
            ('Are your products handmade?', 'Yes. Every piece in our collection is hand-blown by skilled lampworkers and glass artists. Due to the handcrafted nature, slight variations in color, pattern, and dimensions may occur — making each piece truly one of a kind.'),
            ('What does "condition" mean on product listings?', 'We sell both brand-new and pre-owned collector pieces. The condition field indicates whether a piece is New (never used), Like New (minimal use, no defects), or Good (light signs of use). All pre-owned items are thoroughly cleaned and inspected.'),
            ('How do I clean and maintain my glass?', 'We recommend using isopropyl alcohol (90%+) and coarse salt for regular cleaning. Rinse thoroughly with warm water afterwards. Avoid using harsh chemical cleaners. For stubborn residue, soak overnight in a cleaning solution. Regular maintenance keeps your piece looking brand new.'),
            ('Do you offer custom or commissioned pieces?', 'Yes, we work with several talented artists who accept custom commissions. Please reach out via our Contact page with your design ideas, budget, and timeline, and we will connect you with the right artist.'),
        ]
    },
    {
        'name': 'Returns & Refunds',
        'order': 4,
        'faqs': [
            ('What is your return policy?', 'We accept returns within 14 days of delivery for unused items in their original packaging. Custom or commissioned pieces are non-returnable. Please contact our support team to initiate a return.'),
            ('How long does it take to process a refund?', 'Once we receive and inspect your returned item, refunds are processed within 5-7 business days. The refund will be issued to your original payment method. Please allow additional time for your bank to reflect the credit.'),
            ('Do I have to pay for return shipping?', 'Return shipping costs are the responsibility of the buyer unless the item arrived damaged or defective. In those cases, we will provide a prepaid return label at no cost to you.'),
        ]
    },
    {
        'name': 'Account & Support',
        'order': 5,
        'faqs': [
            ('Do I need an account to place an order?', 'No, you can checkout as a guest. However, creating an account allows you to track your orders, save your shipping details for faster checkout, and receive exclusive member-only offers.'),
            ('How do I contact customer support?', 'You can reach us through our Contact page, or by emailing us directly. Our team typically responds within 24 hours during business days. For urgent matters, please indicate so in your message subject line.'),
            ('Do you have a loyalty or rewards program?', 'We occasionally run exclusive promotions and early-access events for our newsletter subscribers. Sign up for our newsletter at the bottom of any page to stay in the loop on special deals and new drops.'),
        ]
    },
]

for cat_data in cats:
    cat = FAQCategory.objects.create(name=cat_data['name'], order=cat_data['order'])
    for i, (q, a) in enumerate(cat_data['faqs']):
        FAQ.objects.create(category=cat, question=q, answer=a, order=i+1)
    print(f"Created category '{cat.name}' with {len(cat_data['faqs'])} FAQs")

print(f"\nDone! Total: {FAQCategory.objects.count()} categories, {FAQ.objects.count()} FAQs")
