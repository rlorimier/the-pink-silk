from django.shortcuts import render
from .models import Packages

# Create your views here.
def all_packages(request):
    """A view to show all the package options available"""

    packages = Packages.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages.html', context)
