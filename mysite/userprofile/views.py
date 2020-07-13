from django.shortcuts import render
from post.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def userprofile(request):
    current_user = request.user
    num_user_posts = Post.objects.filter(author=current_user).count()
    user_posts = Post.objects.filter(author=current_user)
    context = {
    'num_user_posts' : num_user_posts,
    'user_posts' : user_posts,
    }
    return render(request,'profile.html',context=context)
