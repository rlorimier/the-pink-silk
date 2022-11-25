from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Testemonial
from .forms import CommentForm, TestemonialForm


def all_testemonials(request):
    """ A view to show all the testimonials """

    testemonials = Testemonial.objects.all()
    if request.method == "POST":
        comment = CommentForm(data=request.POST)

        if comment.is_valid():
            comment.save()
            messages.success(request, 'Successfully added new comment!')
        else:
            comment = CommentForm()
            messages.success(request, 'Failed to add new comment!')

        context = {
            "testemonials": testemonials,
            "comment": comment,
            "form": CommentForm()
        }

        return render(request, "testemonials.html", context)

    context = {
        'testemonials': testemonials,
        'form': CommentForm()
    }

    return render(request, 'testemonials.html', context)


@login_required
def new_testemonial(request):
    """ A view to add new testimonials """

    if request.method == "POST":
        form = TestemonialForm(request.POST)
        if form.is_valid():
            testemonial = form.save(commit=False)
            testemonial.author = request.user
            testemonial.created_on = timezone.now()
            testemonial.save()
            messages.success(request, 'Successfully added new testimonial!')
            return redirect('testemonials')
        else:
            messages.success(request, 'Failed to add new testimonial.')

    else:
        form = TestemonialForm()

    return render(request, 'new_testemonial.html', {'form': form})
