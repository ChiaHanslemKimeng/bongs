from django.db import models
from .models import Category

def shop_categories(request):
    top_names = ['All Creators', 'Smoking', 'Dabbing', 'Glass Accessories', 'Lifestyle']
    top_categories = Category.objects.filter(name__in=top_names, parent__isnull=True).prefetch_related('children__children')
    
    cases = [models.When(name=name, then=models.Value(i)) for i, name in enumerate(top_names)]
    top_categories = top_categories.annotate(custom_order=models.Case(*cases, output_field=models.IntegerField())).order_by('custom_order')

    return {'shop_top_categories': top_categories}
