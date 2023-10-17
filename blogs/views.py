from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import *
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Posts.objects.all()
    return render(request, "blogs/home.html", {'posts': posts})

# def about(request):
#     return render(request, 'blogs/about.html')

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('blog-home')
    else:
        form = BlogPostForm()
    return render(request, 'blogs/blogpost.html', {'form': form})


@login_required
def delete_blog(request, pk):
    blog_post = get_object_or_404(Posts,pk=pk)

    if request.user == blog_post.author:
        if request.method == 'POST':
            blog_post.delete()
            return redirect('blog-home')
    
        return render(request, 'blogs/deleteblog.html', {'post': blog_post})
    else:
        return render(request, 'blogs/blogdetail.html', {'post': blog_post})


def blog_post_detail(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    return render(request, 'blogs/blogdetail.html', {'post':post})
