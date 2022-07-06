"""RENDER HTML REQUEST"""
from django.shortcuts import render
from django.db.models import Count
from . import models
#Import the exception,
from django.core.exceptions import ObjectDoesNotExist

# def home(request):
#     """
#     The Blog homepage
#     """
#     try:
#         topics_list = models.Topic.objects.filter()
#         #print(topics_list[0],topics_list[1])
#     except ObjectDoesNotExist:
#         print("Error")
#     context = {'TP' : topics_list}
#     #post_list = models.Post.objects.get()

#     return render(request, 'blog/home.html', context)

def home(request):
    # Get last 3 posts
    latest_posts = models.Post.objects.order_by('-published')[:3]
    latest_top = models.Topic.objects.order_by()
    comment_cont = models.Topic.objects.all().annotate(post_count=Count('Post'))
    #authors = models.Post.objects.get_authors()
    # Add as context variable "latest_posts"
    for x in comment_cont:
        print(comment_cont.posts_count)
    context = {'latest_posts': latest_posts,
               'Topics': latest_top,}
    return render(request, 'blog/home.html', context)