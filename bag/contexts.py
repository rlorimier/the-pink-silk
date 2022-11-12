from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    package_count = 0

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'package_count': package_count,
        'grand_total': grand_total,
    }

    return context
