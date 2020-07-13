from django.shortcuts import render
from post.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    num_posts = Post.objects.filter(is_public=True).count()
    public_posts = Post.objects.filter(is_public=True)
    context = {
    'num_posts' : num_posts,
    'public_posts' :  public_posts
    }
    return render(request,'index.html',context=context)
