from django.shortcuts import render , get_object_or_404
from blogs.models import Post


def blogs_view(request):
    posts = Post.objects.filter(status = 1)
    context = {'posts': posts}
    return render(request, 'blogs/blog-home.html', context)

def blogs_single(request,pid):
    posts = Post.objects.filter(status = 1)
    post = get_object_or_404(posts, id = pid)
    context = {'post':post}
    return render(request,'blogs/blog-single.html', context)
