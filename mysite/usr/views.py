from django.shortcuts import render
from django.contrib.auth.models import User
from post.models import Post
# Create your views here.

def usr_index(request):
    num_users = User.objects.count()
    users = User.objects.all()
    context = {
    'num_users':num_users,
    'users':users,
    }
    return render(request,'usr.html',context=context)

def usr_get(request,usr_id):
    num_posts = Post.objects.filter(author_id=usr_id).count()
    usr_posts = Post.objects.filter(author_id=usr_id)

    context = {
    'num_posts':num_posts,
    'usr_posts':usr_posts
    }
    return render(request,'usr_id.html',context=context)
