"""Importing HttpResponse from django.http module"""
from django.http import HttpResponse


def index(request):
    """Function to provide response to HTTP request"""
    return HttpResponse('Welcome Save Soil Page!')
    