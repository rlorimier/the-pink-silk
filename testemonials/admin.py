from django.contrib import admin
from .models import Testemonial, Comment


@admin.register(Testemonial)
class TestemonialAdmin(admin.ModelAdmin):
    """ Admin panel for Testimonials """

    list_display = ('title', 'status', 'created_on', 'pk')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ Admin panel for Comments """

    list_display = ('name', 'body', 'testemonial', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
