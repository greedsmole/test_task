from django.shortcuts import render
from .models import Post
from .forms import NewPostForm,PostForm,updatePostForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import datetime
# Create your views here.

def newpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.is_public = form.cleaned_data['is_public']
            post.author = request.user
            post.created = datetime.data.today()
            post.last_modified = datetime.data.today()
            post.save()
            return HttpResponseRedirect('/profile/')
    else:
        form = PostForm()
    return render(request,'post_form.html',{'form': form })

def updatepost(request,post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = updatePostForm(request.POST)
        if form.is_valid():
            # post = form.save(commit=False)
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.last_modified = datetime.date.today()
            post.created = post.created
            post.is_public = form.cleaned_data['is_public']
            post.null = True
            post.blank = True
            post.save()
            return HttpResponseRedirect("/profile/")
    else:
            form = updatePostForm()
    return render(request,'post_update.html', {'form':form})
