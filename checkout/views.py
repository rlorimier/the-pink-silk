from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.success(
            request, "There's nothing in your bag at the moment"
            )
        return redirect(reverse('packages'))

    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51M5AYmEBzQakth1EVnlWn6i7eXDXMl9DDvExuOWjFvsStWaUvyYpzD9EALpZWWQ8xyPuEaEVpwjOzjDknhuVwDQv00uF2tby3N',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
