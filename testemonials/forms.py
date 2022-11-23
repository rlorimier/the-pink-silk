from .models import Comment, Testemonial
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body',)


class TestemonialForm(forms.ModelForm):
    class Meta:
        model = Testemonial
        fields = ('title', 'content',)
