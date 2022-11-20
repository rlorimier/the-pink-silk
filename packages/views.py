from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def add_package(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.success(
            request, 'Sorry, only store owners can access this page.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PackagesForm(request.POST, request.FILES)
        if form.is_valid():
            package = form.save()
            form.save()
            messages.success(request, 'Successfully added new package!')
            return redirect(reverse('package_detail', args=[package.id]))
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


@login_required
def edit_package(request, package_id):
    """ Edit a package """

    if not request.user.is_superuser:
        messages.success(
            request, 'Sorry, only store owners can access this page.')
        return redirect(reverse('home'))

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


@login_required
def delete_package(request, package_id):
    """ Delete a package """

    if not request.user.is_superuser:
        messages.success(
            request, 'Sorry, only store owners can access this page.')
        return redirect(reverse('home'))

    package = get_object_or_404(Packages, pk=package_id)
    package.delete()
    messages.success(request, 'Package deleted!')
    return redirect(reverse('packages'))
