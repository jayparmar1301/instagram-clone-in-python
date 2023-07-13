from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
# Create your views here.

def hello(request):
    return HttpResponse('Hello, Welcome to my Instagram Clone.')

def detail(request, id):
    user_obj = Posts.objects.get(id = id)
    print(user_obj.user_name, user_obj.caption)
    return HttpResponse(user_obj)