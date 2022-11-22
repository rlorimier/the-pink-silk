from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from packages.models import Packages


def bag_contents(request):
    """ Creates a bag view """

    bag_items = []
    grand_total = total = 0
    package_count = 0

    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        package = get_object_or_404(Packages, pk=item_id)
        total += quantity * package.price
        package_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'package': package,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'package_count': package_count,
        'grand_total': grand_total,
    }

    return context
