"""RENDER HTML REQUEST"""
from django.shortcuts import render
from . import models
from blog.models import Post


def home(request):
    # Get last 3 posts
    latest_posts = models.Post.objects.order_by('-published')[:3]
    latest_top = models.Topic.objects.order_by()

    # Add as context variable "latest_posts"
    context = {'latest_posts': latest_posts,
               'Topics': latest_top}
    return render(request, 'blog/home.html', context)
