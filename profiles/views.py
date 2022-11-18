from django.shortcuts import render


def profile(request):
    """ Display the user's profile. """

    template = 'profile.html'
    context = {}

    return render(request, template, context)
