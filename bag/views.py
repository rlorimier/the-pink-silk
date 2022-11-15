from django.shortcuts import (
    render, redirect, reverse, HttpResponse
    )
from django.contrib import messages
from packages.models import Packages


def view_bag(request):
    """A view to show the shopping bag"""

    return render(request, 'bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified package to the shopping bag """

    package = Packages.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'Package { package.name } successfully updated'
            )
    else:
        bag[item_id] = quantity
        messages.success(
            request, f'Package { package.name } successfully added to the bag'
            )

    request.session['bag'] = bag
    # print(request.session['bag'])
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified item"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
