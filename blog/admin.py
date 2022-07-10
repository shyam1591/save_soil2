#from xml.etree.ElementTree import Comment
from django.contrib import admin

# Register your models here.
from . import models
from .models import Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):

    """Display Fields"""
    list_display = (
        'title',
        'created',
        'updated',
        'author'
    )
    prepopulated_fields = {"slug": ("title",)}
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
    prepopulated_fields = {"slug": ("name",)}


class PostComment(admin.ModelAdmin):
    list_display = (
        'post',
        'name',
        'email',
        'text',
        'approved',
        # 'created',
        # 'updated',
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

    def comment_approve(self, query):
        query.update(True)


# Register the `Post` model
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Topic, PostTopic)
admin.site.register(models.Comment, PostComment)
