from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from .forms import PostForm 
from django.utils import timezone

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_list2(requests):
    ls=Post.objects.all()
    s="<ul>"
    for item in ls:
        s+="<li>"+str(item)+"</li>"
    s+="</ul>"
    return HttpResponse(s)

def post_list(requests):
    ls=Post.objects.all()
    content = {"posts":ls}
    return render(requests,'blog/post_list.html',content)


def create100(requests):
    me = User.objects.get(username='admin')
    for i in range(100):
        p=Post.objects.create(author=me, title=f'Sport{i}', text=f'football iran VS hongkong{i}')

        p.publish()
    return HttpResponse("Done")