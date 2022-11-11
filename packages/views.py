from django.shortcuts import render, get_object_or_404
from .models import Packages


def all_packages(request):
    """A view to show all the package options available"""

    packages = Packages.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages.html', context)


def package_detail(request, package_id):
    """A view to show the package details"""

    package = get_object_or_404(Packages, pk=package_id)

    context = {
        'package': package,
    }

    return render(request, 'package_detail.html', context)
