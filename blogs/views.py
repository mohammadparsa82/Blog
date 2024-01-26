from django.shortcuts import render , get_object_or_404
from blogs.models import Post


def blogs_view(request):
    posts = Post.objects.filter(status = 1)
    context = {'posts': posts}
    return render(request, 'blogs/blog-home.html', context)

def blogs_single(request,pid):
    post = get_object_or_404(Post, id = pid)
    context = {'post':post}
    return render(request,'blogs/blog-single.html', context)
