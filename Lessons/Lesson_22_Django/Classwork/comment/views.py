from django.shortcuts import render
from django.http import HttpResponse


def comment_page(request):
    return HttpResponse('This is an comment page!')
