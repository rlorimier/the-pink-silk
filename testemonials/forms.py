from .models import Comment, Testemonial
from django import forms


class CommentForm(forms.ModelForm):
    """ A form to handle comments from all users """

    class Meta:
        model = Comment
        fields = ('name', 'body',)


class TestemonialForm(forms.ModelForm):
    """ A form to handle testimonials from registered users """

    class Meta:
        model = Testemonial
        fields = ('title', 'content',)
