from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm

@login_required
def dashboard(request):
    # Fetch user's orders
    orders = request.user.orders.all()
    completed_orders = orders.filter(paid=True).count()
    
    return render(request, 'accounts/dashboard.html', {
        'orders': orders,
        'completed_orders': completed_orders,
    })

@login_required
def profile_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('accounts:dashboard')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'accounts/profile_update.html', {'form': form})
