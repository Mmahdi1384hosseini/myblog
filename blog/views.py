from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User

def create100(requests):
    me = User.objects.get(username='admin')
    for i in range(100):
        Post.objects.create(author=me, title='sport', text='football iran VS hongkong')

    # p=Post()
    # p.text='football iran VS hongkong'
    # p.title='sport'
    # p.author=User
    # p.publish()
    return HttpResponse("Done")