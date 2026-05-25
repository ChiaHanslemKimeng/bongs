from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # Fetch user's orders
    orders = request.user.orders.all()
    completed_orders = orders.filter(paid=True).count()
    
    return render(request, 'accounts/dashboard.html', {
        'orders': orders,
        'completed_orders': completed_orders,
    })
