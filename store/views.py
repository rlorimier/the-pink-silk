from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.contrib import messages


def index(request):
    """A view to show the home page"""

    return render(request, 'index.html')


def about(request):
    """A view to show the about us page"""

    aboutus = ""
    return render(request, 'about.html', {'aboutus': aboutus})


def contact(request):
    """A view to show the contact form page"""

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Contact request received!')
            return redirect(reverse('contact'))
        else:
            messages.success(
                request,
                'Contact request failed. Please ensure the form is valid!')

    else:
        form = ContactForm()

    return render(request, "contact.html", {'form': form})
