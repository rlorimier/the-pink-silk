from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Testemonial
from .forms import CommentForm, TestemonialForm


def all_testemonials(request):
    """ A view to show all the testimonials """
    testemonials = Testemonial.objects.all()
    
    if request.method == "POST":
        comment = CommentForm(data=request.POST)

        if comment.is_valid():
            #comment.name = request.name
            #comment.body = request.body
            comment.save()
        else:
            comment = CommentForm()

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

# def comment(request):

#     if request.method == "POST":
#         comment = CommentForm(data=request.POST)

#         if comment.is_valid():
#             comment.name = request.name
#             comment.body = request.body
#             comment.save()
#         else:
#             comment = CommentForm()

#         context = {
#             "testemonials": testemonials,
#             "comment": comment,
#             "form": CommentForm()
#         }

#         return render(request, "testemonials.html", context)


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






# class PostList(View):
#     def get(self, request, slug, *args, **kwargs):
#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         comments = post.comments.filter(approved=True).order_by("-created_on")
#         liked = False
#         if post.likes.filter(id=self.request.user.id).exists():
#             liked = True

#         return render(
#             request,
#             "testemonials.html",
#             {
#                 "post": post,
#                 "comments": comments,
#                 "commented": False,
#                 "liked": liked,
#                 "comment_form": CommentForm()
#             },
#         )

#     def post(self, request, slug, *args, **kwargs):
#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         comments = post.comments.filter(approved=True).order_by("-created_on")
#         liked = False
#         if post.likes.filter(id=self.request.user.id).exists():
#             liked = True

#         comment_form = CommentForm(data=request.POST)

#         if comment_form.is_valid():
#             comment_form.instance.email = request.user.email
#             comment_form.instance.name = request.user.username
#             comment = comment_form.save(commit=False)
#             comment.post = post
#             comment.save()
#         else:
#             comment_form = CommentForm()

#         return render(
#             request,
#             "testemonials.html",
#             {
#                 "post": post,
#                 "comments": comments,
#                 "commented": True,
#                 "liked": liked,
#                 "comment_form": CommentForm()
#             },
#         )


# class PostLike(View):

#     def post(self, request, slug):
#         post = get_object_or_404(Post, slug=slug)

#         if post.likes.filter(id=request.user.id).exists():
#             post.likes.remove(request.user)
#         else:
#             post.likes.add(request.user)

#         return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# def new_testemonial(request):

#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.created_on = timezone.now()
#             post.save()
#             return redirect('index')
#         else:
#             messages.success(request, 'Failed to add new post.')

#     else:
#         form = PostForm()

#     return render(request, 'new_testemonial.html', {'form': form})
