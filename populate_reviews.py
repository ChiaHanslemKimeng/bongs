import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Review

def populate():
    Review.objects.all().delete()
    
    reviews_data = [
        ("Alex J.", 5, "Absolutely stunning piece of glass. The beaker hits so smooth and it looks like a work of art on my coffee table."),
        ("Sarah T.", 5, "Shipping was fast and the packaging was super secure. The matrix perc is a game changer for flavor!"),
        ("Mike D.", 4, "Great straight tube, very thick borosilicate. Minus one star because it's almost too heavy!"),
        ("Emily R.", 5, "I bought the Tornado Recycler and it is mesmerizing. Every session is an experience. Highly recommend."),
        ("Jordan K.", 5, "The honeycomb percolator stacks bubbles like crazy. Best bong I've ever owned, hands down."),
        ("Chloe M.", 5, "Customer service was fantastic when I had a question about joint sizes. The rig itself is flawless."),
        ("Dave W.", 4, "Solid piece, thick glass. Took a bit longer to arrive but totally worth the wait for this quality."),
        ("Anna S.", 5, "A beautiful intersection of modern design and functional glass. This is truly a luxury smoking accessory."),
        ("Lucas P.", 5, "The 18-inch beaker clears so easily. You can tell real artisans blew this glass. Flawless joints."),
        ("Mia C.", 5, "I was hesitant about the price but the craftsmanship is undeniable. The hits are incredibly smooth."),
        ("Tyler L.", 5, "Perfect rig for concentrates. The flavor saver aspect is real. Love the minimalist aesthetic."),
        ("Olivia B.", 4, "Beautiful piece. The inline perc is super smooth, though cleaning it requires some patience and iso."),
        ("Ethan H.", 5, "This is my daily driver now. The weight and feel of the glass justify the premium brand positioning."),
        ("Ava N.", 5, "Bought the mini rig and it hits like a dream. Highly functional and beautiful to look at."),
        ("Ryan F.", 5, "The thick base on the beaker bong makes it virtually tip-proof. Incredible build quality."),
        ("Sophia G.", 5, "Exquisite glassware! Even the packaging felt luxurious. I'm proud to display this in my living room."),
        ("Zack V.", 4, "Great pull, good percolation. I just wish there were more color options instead of just clear."),
        ("Isabella R.", 5, "Elias Vance's work is unmatched. This custom piece is the highlight of my collection."),
        ("Nathan E.", 5, "The ash catcher add-on is a must. Keeps the main tube pristine. Excellent airflow throughout."),
        ("Grace T.", 5, "I’ve gone through many bongs, but the thick borosilicate on this one feels indestructible."),
        ("Leo J.", 5, "Everything about this brand screams luxury. The draw is effortless and the glass is crystal clear."),
        ("Lily K.", 5, "Just an amazing product. The straight tube delivers direct, massive hits without harshness."),
        ("Caleb M.", 5, "If you want a centerpiece that also functions perfectly, this is it. No regrets."),
        ("Zoe L.", 4, "Very high quality. I accidentally bumped it against my sink while cleaning and it didn't even scratch."),
        ("Mason W.", 5, "Best glass investment I've made. The percolation science they talk about really translates to the smoke."),
        ("James P.", 5, "Unbelievable craftsmanship, this rig totally changed my dab game."),
        ("Lisa R.", 4, "A bit pricey, but the quality of the glass is fantastic and it looks amazing.")
    ]

    base_date = datetime.now() - timedelta(days=60)
    
    for idx, (author, rating, text) in enumerate(reviews_data):
        created = base_date + timedelta(days=idx*2)
        r = Review.objects.create(author_name=author, rating=rating, content=text)
        r.created_at = created
        r.save()

    print("Successfully populated 25 reviews.")

if __name__ == '__main__':
    populate()
