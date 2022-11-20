from django.shortcuts import render


# Create your views here.
def index(request):
    """A view to show the home page"""

    return render(request, 'index.html')


def about(request):
    """A view to show the about us page"""

    aboutus = ""
    return render(request, 'about.html', {'aboutus': aboutus})
