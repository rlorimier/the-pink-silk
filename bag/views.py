from django.shortcuts import render


def view_bag(request):
    """A view to show the shopping bag"""

    return render(request, 'bag.html')
