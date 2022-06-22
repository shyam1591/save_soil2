from cgitb import text
from msilib.schema import Class
from xml.etree.ElementTree import Comment
from django.contrib import admin

# Register your models here.
from . import models

class PostAdmin(admin.ModelAdmin):
    """Display Fields"""
    list_display = (
        'title',
        'created',
        'updated',
        'author'
    )

    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )

    list_filter = (
        'status',
        'topic',
    )

class PostTopic(admin.ModelAdmin):
    """Display Fields"""
    list_display = (
        'name',
        'slug'
    )

class CommentInline(admin.StackedInline):
    model = Comment
    readonly_fields = ('name','text','email')
    extra = 0


class PostComment(admin.ModelAdmin):
    list_display = (
        'post',
        'name',
        'email',
        'text',
        'approved',
        #'created',
        #'updated',
    )

    search_fields = (
        'post',
        'name',
        'email',
        'text',
        'approved',
        'created',
        'updated',
    )

    def comment_approve(self,query):
        query.update(True)


# Register the `Post` model
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Topic, PostTopic)
admin.site.register(models.Comment, PostComment)