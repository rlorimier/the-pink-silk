from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Packages
from .forms import PackagesForm


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


def add_package(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = PackagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added new package!')
            return redirect(reverse('add_package'))
        else:
            messages.success(
                request,
                'Failed to add package. Please ensure the form is valid.')
    else:
        form = PackagesForm()

    template = 'add_package.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_package(request, package_id):
    """ Edit a package """
    package = get_object_or_404(Packages, pk=package_id)
    if request.method == 'POST':
        form = PackagesForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated package!')
            return redirect(reverse('package_detail', args=[package.id]))
        else:
            messages.success(
                request, 
                'Failed to update package. Please ensure the form is valid.')
    else:
        form = PackagesForm(instance=package)
        messages.success(request, f'You are editing {package.name}')

    template = 'edit_package.html'
    context = {
        'form': form,
        'package': package,
    }

    return render(request, template, context)
