from django.shortcuts import render
from .models import Post,User

# Create your views here.

def index(request):
    posts = Post.get_posts()
    return render(request, 'index.html', {"posts": posts})

def profile(request, id):
    profiles = User.open_profile(id)
    feeds = Post.get_feed(id)
    return render(request, 'profile.html', {"profiles": profiles , "feeds": feeds})